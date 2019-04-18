<template>
    <v-dialog max width="1450px" v-model="dialog">
        <v-btn round style="border-radius:7px;" slot="activator" class="info">Add new post</v-btn>
            <v-layout row wrap>
            <v-card min width="725px" class="px-5">
                <v-card-title>
                    <h2>Add Blog Post</h2>
                </v-card-title>
                <v-card-text>
                    <v-form ref="form">
                        <v-text-field label="Title" v-model="title" prepend-icon="folder" :rules="inputRules"></v-text-field>
                        <v-textarea label="Information" v-model="content" prepend-icon="edit" :rules="inputRules"></v-textarea>

                        <v-menu>
                            <v-text-field disabled :value="date" slot="activator" label="Date" prepend-icon="date_range"></v-text-field>
                            <!--<v-date-picker v-model="date"></v-date-picker>-->
                        </v-menu>
                        
                        <v-spacer></v-spacer>

                        <v-btn flat round style="border-radius:7px;" class="info mx-3 mt-3" @click="publish" :loading="loading">Save and Publish</v-btn>
                        <v-btn flat round style="border-radius:7px;" class="info mx-0 mt-3" @click="dialog = false">Cancel</v-btn>
                    </v-form>
                </v-card-text>
            </v-card>
             <v-card min width="725px" class="px-5">
                <v-card-title>
                    <h2>Preview</h2>
                </v-card-title>
                <v-card-text>
                    <h2>{{ title }}</h2>
                    <v-layout row justify-start align-start>
                        <v-flex class="caption grey--text">Written by {{ user }}</v-flex>
                        <v-flex class="caption grey--text">Published on {{ date }}</v-flex>
                    </v-layout>
                    <br>
                    <p>{{ content }}</p>
                </v-card-text>
            </v-card>
            </v-layout>
    </v-dialog>
</template>

<script>
//import axios from 'axios'
import db from '@/fb'
//import moment from 'moment'
export default {
    data() {
        return {
            title: '',
            content: '',
            //date: new Date().toDateString() - puts date in words
            date: new Date().toISOString().substr(0, 10),
            inputRules: [
                v => v.trim() !== '' || 'You cannot leave this empty'
            ],
            // controls when the loading sign appears on the button
            loading: false,
            // closes the add post window/pop up
            dialog: false,
            // array of blog posts
            posts: [],
            // hard-coded user - change later
            user: 'Tom'
        }
    },
    methods: {
        publish() {
            if(this.$refs.form.validate()) {
                //use this when we actually put it in the database to show a loading sign
                this.loading = true; 
                
                const newBlogPost = {
                    title: this.title,
                    content: this.content,
                    date: this.date,
                    user: this.user
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
                this.dialog = false;
                // alert snackbox to show user that the blog post was published
                this.$emit('blogPostAdded')
                
                /*
                console.log(newBlogPost);
                let post = this;
                // store in database via a post method
                axios.post('http://127.0.0.1:5000/blog', {
                    title: this.title,
                    content: this.content,
                    date: this.date
                })
                // if the response is correct
                .then((response) => {
                    console.log(response);
                })
                // if the response is incorrect
                .catch((error) => {
                    console.log(error);
                });
                // stop loading and close the window
                this.loading = false;
                this.dialog = false;
                this.$emit('blogPostAdded')*/
            }
        },
    }
}
</script>