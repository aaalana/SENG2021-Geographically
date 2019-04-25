<template>
    <v-dialog persistent no-click-animation max width="100%" v-model="dialog">
        <v-btn round style="border-radius:7px;" slot="activator" class="info" @click="turnOffErrorChecking"><b>Add new post</b></v-btn>
            <v-layout row wrap>
            <v-card max width="50%" class="px-5">
                <br><br>
                <v-card-title>
                    <h2 style='font-family:Quicksand;'>Add Blog Post</h2>
                </v-card-title>
                <v-card-text>
                    <v-form ref="form">
                        <v-text-field counter="20" label="Title" v-model="title" prepend-icon="folder" :rules="[rules.empty, rules.max2]"></v-text-field><br>
                        <v-textarea v-show=false label="Tell us about your trip" v-model="content" prepend-icon="edit" :rules="rules.empty"></v-textarea>
                        <quill-editor id="quill" :options="editorOption" ref="myQuillEditor" v-model="content" @input="isQuillEmpty"/>
                        <v-flex v-model= "contentError" v-if="contentError === true" style="border-top-style: solid; border-width: thin; padding-top:5px; font-size:13px; color:red;">This field cannot be empty</v-flex>

                        <v-text-field label="Rate the location you visited (optional)" counter="25" :rules="rules.max" v-model="rateLoc" prepend-icon="location_on"></v-text-field>
                       
                        <v-layout>
                            <v-spacer></v-spacer>
                            <span class="grey--text text--lighten-1 mr-2">({{ rating }})</span>
                            <v-rating
                                v-model="rating"
                                background-color="yellow accent-4"
                                color="yellow accent-4"
                                dense
                                half-increments
                                hover
                                size="20"
                            ></v-rating>
                        </v-layout>

                        <v-menu>
                            <v-text-field disabled :value="date" slot="activator" label="Date" prepend-icon="date_range"></v-text-field>
                        </v-menu>
                        <v-spacer></v-spacer>

                        <v-btn flat round style="border-radius:7px;" class="info mx-3 mt-3" @click="publish" :loading="loading">Save and Publish</v-btn>
                        <v-btn flat round style="border-radius:7px;" class="info mx-0 mt-3" @click="reset">Cancel</v-btn>
                    </v-form>
                </v-card-text>
                </v-card>
           
                <v-card max width="50%" class="px-5">
                    <br><br>
                    <v-card-title>
                        <h2 style='font-family:Quicksand;'>Preview</h2>
                    </v-card-title>
                    <v-card-text>
                        <link href='https://fonts.googleapis.com/css?family=Quicksand' rel='stylesheet'>
                        <h2 style="font-family:Quicksand; word-wrap: break-word;">{{ title }}</h2>
                        <v-layout row justify-start align-start>
                            <v-flex pr-4 xs4 md4 class="caption grey--text" style="word-wrap: break-word;">Written by {{ user }}</v-flex>
                            <v-flex xs4 md4 class="caption grey--text" style="word-wrap: break-word;">Modified on {{ date }}</v-flex>
                            <v-flex xs4 md4 class="caption grey--text" style="word-wrap: break-word;">
                                
                                <div class="caption grey--text" style="word-wrap: break-word;"><v-icon small class="mr-1">location_on</v-icon>{{ rateLoc }}</div>
                              
                                <v-rating
                                class="ml-3"
                                v-model="rating"
                                background-color="yellow accent-4"
                                color="yellow accent-4"
                                dense
                                small
                                half-increments
                                readonly
                                size="20"
                                ></v-rating>
                                
                            </v-flex>
                        </v-layout>
                        <br>
                        <div style="word-wrap: break-word;" v-html="compiledHTML"></div>
                    </v-card-text>
                </v-card>
        </v-layout>
    </v-dialog>
</template>

<script>
import 'quill/dist/quill.snow.css'
import db from '@/fb'
import { quillEditor } from 'vue-quill-editor'
var sanitizeHtml = require('sanitize-html');

var toolbarOptions= [
                        ['bold', 'italic', 'underline', 'strike'],        // toggled buttons
                        ['blockquote', 'code-block'],
                        [{ 'header': 1 }, { 'header': 2 }],               // custom button values
                        [{ 'list': 'ordered'}, { 'list': 'bullet' }],
                        [{ 'direction': 'rtl' }],                         // text direction

                        [{ 'size': ['small', false, 'large', 'huge'] }],  // custom dropdown
                        [{ 'header': [1, 2, 3, 4, 5, 6, false] }],

                        [{ 'color': [] }, { 'background': [] }],          // dropdown with defaults from theme
                        [{ 'font': [] }],
                        [{ 'align': [] }],

                        ['clean'],                                         // remove formatting button
                        ['link', 'video']
                    ];

export default {
    components: {
        quillEditor
    },
    data() {
        return {
            title: '',
            content: '',
            //date: new Date().toDateString() - puts date in words
            date: new Date(new Date().toString().split('GMT')[0]+' UTC').toISOString().split('T')[0],
            rules: {
                empty: v => v.trim() !== '' || 'This field cannot be empty',
                max: v => v.length <= 25 || 'Max 25 characters',
                max2: v => v.length <= 25 || 'Max 20 characters'
            },
            // controls when the loading sign appears on the button
            loading: false,
            // closes the add post window/pop up
            dialog: false,
            // array of blog posts
            posts: [],
            user: 'John',
            rating: 1,
            contentError: false,
            rateLoc: '',
            editorOption: {
                debug: 'info',
                placeholder: 'Tell us about your trip :)',
                readOnly: false,
                theme: 'snow',
                modules: {
                    toolbar: toolbarOptions
                }
            },
            cancel: false
        }
    },
    methods: {
        publish() {
            this.isQuillEmpty();
            if(this.$refs.form.validate() && this.contentError === false) {
                //use this when we actually put it in the database to show a loading sign
                this.loading = true; 
                const newBlogPost = {}
                // side notee: could try to sanitize all tags to just get the text content
                if (this.rateLoc === '') {
                    newBlogPost.title = this.title;
                    newBlogPost.content= this.compiledHTML;
                    newBlogPost.date= this.date;
                    newBlogPost.user= this.user;
                    newBlogPost.rating= 0;
                    newBlogPost.locationRated= '';
                      
                } else {
                    newBlogPost.title= this.title;
                    newBlogPost.content= this.compiledHTML;
                    newBlogPost.date= this.date;
                    newBlogPost.user= this.user;
                    newBlogPost.rating= this.rating;
                    newBlogPost.locationRated= this.rateLoc;
                    
                }
              
                // add to firebase
                db.collection('posts').add(newBlogPost).then(() => {
                    console.log('blog post added successfully');
                })
                .catch(error => {
                    console.log(error);
                })
                // stop loading and close the window
                this.loading = false;
                this.reset();
                // alert snackbox to show user that the blog post was published
                this.$emit('blogPostAdded');
            }
        },
        // reset the text field 
        reset() {
            this.dialog = false; 
            this.cancel = true;
            //this.$refs.form.reset(this.title, this.content) resets everything
            this.title = '';
            this.content = '';
            this.contentError = false;
            this.rating = 1;
            this.rateLoc = '';
            this.$refs.form.resetValidation();
        },
        isQuillEmpty() {
            if (this.cancel === false && this.$refs.myQuillEditor.quill.getText().trim().length === 0 && 
                this.$refs.myQuillEditor.quill.container.firstChild.innerHTML.includes("img") === false &&
                this.$refs.myQuillEditor.quill.container.firstChild.innerHTML.includes("iframe") === false) {
                    return this.contentError = true;
            } else {
                    return this.contentError = false;
            }
        },
        turnOffErrorChecking() {
            this.contentError = false;
            this.cancel = false;
        }
    },
    computed: {
        compiledHTML: function() {
            var clean = sanitizeHtml(this.content, {
                allowedTags: [ 'p', 'a', 'em', 'strong','u', 'iframe', 'ul', 'ol', 'h1', 'h2','h3', 'h4', 'h5', 'h6', 'blockquote', 's', 'li','class', 'span', 'br'],
                allowedAttributes: {
                    a: [ 'href', 'name', 'target'],
                    p: ['class'],
                    span: ['class', 'style'],
                    iframe: ['class', 'frameborder', 'allowfullscreen', 'src'],
                },
                allowedClasses: {
                    'p': ['ql-align-right', 'ql-direction-rtl','ql-align-justify', 'ql-align-center', 'ql-align-right'],
                    'span': ['ql-size-huge','ql-size-small', 'ql-size-large','ql-cursor',
                             'ql-font-serif','ql-font-monospace'],
                    'iframe': ['ql-video']
                },
                allowedStyles: {
                    '*': {
                        // only allow rgb (from the quill toolbar)
                        'color': [/^rgb\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)$/],
                        'background-color':[/^rgb\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)$/]
                    }
                },
                allowedIframeHostnames: ['www.youtube.com'],
                allowedSchemesByTag: {},
                allowedSchemesAppliedToAttributes: [ 'href', 'src', 'cite' ],
                allowProtocolRelative: true,
                allowIframeRelativeUrls: true,
                nonTextTags: [ 'style', 'script', 'textarea', 'noscript' ]
            });
            return clean
        }
    }
}

</script>

<style>
.ql-size-small {
    font-size: small;
}

.ql-size-large {
    font-size: large;
}

.ql-size-huge {
    font-size: x-large;
}

.ql-font-serif {
    font-family: serif;
}

.ql-font-monospace {
    font-family: monospace;
}

.ql-align-center {
    text-align: center;
}

.ql-align-right {
    text-align: right;
}

.ql-align-justify {
    text-align: justify;
}

.ql-direction-rtl {
    direction: rtl;
}

.ql-editor {
    height: 30vh;
    
}

#ql-container {
    resize: vertical;
    overflow-y: scroll;
    
}

blockquote {
  display: block;
  margin-top: 1em;
  margin-bottom: 1em;
  margin-left: 40px;
  margin-right: 40px;
}
</style>