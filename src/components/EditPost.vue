<template>
    <v-dialog persistent no-click-animation max width="100%" v-model="dialog">
        <v-btn flat fab slot="activator"><v-icon>edit</v-icon></v-btn>
            <v-layout row wrap>
            <v-card max width="50%" class="px-5">
                <br><br>
                <v-card-title>
                     <h2 style='font-family:Quicksand;'>Edit Blog Post</h2>
                </v-card-title>
                <v-card-text>
                    <v-form ref="form">
                        <v-text-field label="Title" v-model="editedTitle" prepend-icon="folder" :rules="inputRules"></v-text-field><br>
                        <!--<v-textarea label="Tell us about your trip" v-model="editedContent" prepend-icon="edit" :rules="inputRules"></v-textarea>-->
                        <quill-editor id="quill" :options="editorOption" ref="myQuillEditor" v-model="editedContent" @input="isQuillEmpty"/>
                        <v-flex v-model= "contentError" v-if="contentError === true" style="border-top-style: solid; border-width: thin; padding-top:5px; font-size:13px; color:red;">This field cannot be empty</v-flex>

                        <v-text-field label="Rate the location you visited (optional)" counter="25" :rules="locRules" v-model="rateLoc" prepend-icon="location_on"></v-text-field>
                        <br>
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

                        <v-btn flat class="info mx-3 mt-3" @click="publish" :loading="loading">Save and Publish</v-btn>
                        <v-btn flat round style="border-radius:7px;" class="info mx-0 mt-3"  @click="reset">Cancel</v-btn>
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
                    <h2 style="font-family:Quicksand; word-wrap: break-word;">{{ editedTitle }}</h2>
                    <v-layout row justify-start align-start>
                        <v-flex pr-4 xs6 md6 class="caption grey--text" style="word-wrap: break-word;">Written by {{ user }}</v-flex>
                        <v-flex xs6 md6 class="caption grey--text" style="word-wrap: break-word;">Modified on {{ date }}</v-flex>
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
    // used to retrieve data found on blog.vue via :post
    components: {
        quillEditor
    },
    props: ['post'],
    data() {
        return {
            // load the data from the post array via props
            editedTitle: this.post.title,
            editedContent: this.post.content,
            date: new Date(new Date().toString().split('GMT')[0]+' UTC').toISOString().split('T')[0],
            inputRules: [
                v => v.trim() !== '' || 'This field cannot be empty'
            ],
            locRules: [v => v.length <= 25 || 'Max 25 characters'],
            loading: false, // controls when the loading sign appears on the button
            dialog: false, // closes the add post window/pop up
            postId: this.post.id, // array of blog posts
            user: 'Tom',  // hard-coded user - change later
            rating: this.post.rating,
            rateLoc: this.post.locationRated,
            hasupdated: false,
            contentError: false,
            editorOption: {
                debug: 'info',
                placeholder: 'Tell us about your trip :)',
                readOnly: false,
                theme: 'snow',
                modules: {
                    toolbar: toolbarOptions
                }
            }
        }
    },
    methods: {
        publish() {
            if(this.$refs.form.validate() && this.madeChanges() === true && this.contentError === false) {
                //use this when we actually put it in the database to show a loading sign
                this.loading = true; 
               
                const update = {}
                // only update the changes made
                if (this.editedTitle !== this.post.title) {
                    update.title = this.editedTitle;
                    this.hasupdated = true;
                }

                if (this.compiledHTML !== this.post.content) {
                    update.content = this.compiledHTML;
                    this.hasupdated = true;
                }

                if (this.rateLoc === '' && this.rateLoc !== this.post.locationRated) {
                    update.locationRated = this.rateLoc;
                    update.rating = 0;
                    this.hasupdated = true;
                } else if (this.rateLoc !== this.post.locationRated) {
                    update.locationRated = this.rateLoc;
                    update.rating = this.rating;
                    this.hasupdated = true;
                } else if (this.rating !== this.post.rating) {
                    update.rating = this.rating;
                    this.hasupdated = true;
                }
                
                if (this.hasupdated === true) {
                    update.date  = new Date(new Date().toString().split('GMT')[0]+' UTC').toISOString().split('T')[0];
                }

                // delete post from the database
                db.collection('posts').doc(this.postId).update(update).then(function() {
                    console.log("Post successfully updated!");
                }).catch(function(error) {
                    console.error("Error editing post: ", error);
                });
               
                // stop loading and close the window
                this.loading = false;
                this.dialog = false;
                this.$emit('blogPostUpdated')
                this.$emit('updateFrontEnd')
            }
        },
        // reset editing stage 
        reset() {
            this.dialog = false,
            this.editedTitle = this.post.title,
            this.editedContent = this.post.content,
            this.rating= this.post.rating,
            this.rateLoc= this.post.locationRated,
            this.contentError = false
        },
        // check if any changes when editing the blog post was made
        madeChanges() {
            if (this.editedTitle === this.post.title && 
                this.editedContent === this.post.content && 
                this.rateLoc === this.post.locationRated &&
                this.rating === this.post.rating) {
                    this.$emit('blogPostNotUpdated')
                    return false;
            } else {
                return true;
            }
        },
        isQuillEmpty() {
            if (this.$refs.myQuillEditor.quill.getText().trim().length === 0 && 
                this.$refs.myQuillEditor.quill.container.firstChild.innerHTML.includes("img") === false &&
                this.$refs.myQuillEditor.quill.container.firstChild.innerHTML.includes("iframe") === false) {
                    return this.contentError = true;
            } else {
                    return this.contentError = false;
            }
        }
    },
    computed: {
        compiledHTML: function() {
            var clean = sanitizeHtml(this.editedContent, {
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
                allowedSchemes: ['https'],
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

.ql-container {
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