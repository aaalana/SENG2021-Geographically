<template>
    <v-dialog persistent no-click-animation max width="100%" v-model="dialog">
        <v-btn round style="border-radius:7px;" slot="activator" class="info"><b>Add new post</b></v-btn>
            <v-layout row wrap>
            <v-card max width="50%" class="px-5">
                <br><br>
                <v-card-title>
                    <h2 style='font-family:Quicksand;'>Add Blog Post</h2>
                </v-card-title>
                <v-card-text>
                    <v-form ref="form">
                        <v-text-field label="Title" v-model="title" prepend-icon="folder" :rules="inputRules"></v-text-field>
                        <v-textarea label="Tell us about your trip" v-model="content" prepend-icon="edit" :rules="inputRules"></v-textarea>
                        <quill-editor :rules="inputRules" id="quill" :options="editorOption" ref="myQuillEditor" v-model="content" />
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

                        <v-btn flat round style="border-radius:7px;" class="info mx-3 mt-3" @click="publish" :loading="loading">Save and Publish</v-btn>
                        <v-btn flat round style="border-radius:7px;" class="info mx-0 mt-3" @click="reset">Cancel</v-btn>
                    </v-form>
                </v-card-text>
                </v-card>
           
                <v-card width="50%" class="px-5">
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
                        <div style="word-wrap: break-word;" v-html='compiledHTML'></div>
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
            inputRules: [
                v => v.trim() !== '' || 'You cannot leave this empty'
            ],
            locRules: [v => v.length <= 25 || 'Max 25 characters'],
            // controls when the loading sign appears on the button
            loading: false,
            // closes the add post window/pop up
            dialog: false,
            // array of blog posts
            posts: [],
            // hard-coded user - change later
            user: 'Tom',
            rating: 1,
            rateLoc: '',
            editorOption: {
                debug: 'info',
                placeholder: 'Tell us about your trip :)',
                readOnly: false,
                theme: 'snow'
            }/*,
            cleanContent: sanitizeHtml(this.content, {
                allowedTags: [ 'h1', 'h2', 'blockquote', 'p', 'a', 'ul', 'ol',
  'nl', 'li', 'b', 'i', 'strong', 'em', 'strike', 'code', 'hr', 'br', 'div',
  'table', 'thead', 'caption', 'tbody', 'tr', 'th', 'td', 'pre', 'iframe' ],
                allowedAttributes: {
                    'a': [ 'href' ]
                },
                allowedIframeHostnames: ['www.youtube.com']
            })*/
        }
    },
    methods: {
        publish() {
            if(this.$refs.form.validate()) {
                //use this when we actually put it in the database to show a loading sign
                this.loading = true; 
                const newBlogPost = {}
                if (this.rateLoc === '') {
                    newBlogPost.title = this.title;
                    newBlogPost.content= this.content;
                    newBlogPost.date= this.date;
                    newBlogPost.user= this.user;
                    newBlogPost.rating= 0;
                    newBlogPost.locationRated= '';
                      
                } else {
                    newBlogPost.title= this.title;
                    newBlogPost.content= this.content;
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
            //this.$refs.form.reset(this.title, this.content) resets everything
            this.title = '';
            this.content = '';
            this.rating = 1;
            this.rateLoc = '';
            this.$refs.form.resetValidation();
        }/*,
        convertHTML() {

            var justHtmlContent = document.getElementById('justHtml');

                var delta = editor.getContents();
                //var text = editor.getText();
                var justHtml = editor.root.innerHTML;
                //preciousContent.innerHTML = JSON.stringify(delta);
                //justTextContent.innerHTML = text;
                justHtmlContent.innerHTML = justHtml;
                this.delta*
        
    }*/
              //  this.delta = this.$refs.myQuillEditor.quill.getContent();
         
    },
    computed: {
        compiledHTML: function() {
            return this.content
        }
    }
    
}
</script>

<style>
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

.ql-container {
    resize: vertical;
    overflow-y: scroll;
    
}

.ql-syntax {
    background-color: black;
    font-family: monospace;
    color: white;
    padding: 5px;
    border-radius: 5px;
}

blockquote {
  display: block;
  margin-top: 1em;
  margin-bottom: 1em;
  margin-left: 40px;
  margin-right: 40px;
}
</style>