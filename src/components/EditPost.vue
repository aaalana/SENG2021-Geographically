<template>
    <v-dialog max width="1450px" v-model="dialog">
        <v-btn flat fab slot="activator"><v-icon>edit</v-icon></v-btn>
            <v-layout row wrap>
            <v-card min width="725px" class="px-5">
                <v-card-title>
                    <h2>Edit Blog Post</h2>
                </v-card-title>
                <v-card-text>
                    <v-form ref="form">
                        <v-text-field label="Title" v-model="editedTitle" prepend-icon="folder" :rules="inputRules"></v-text-field>
                        <v-textarea label="Information" v-model="editedContent" prepend-icon="edit" :rules="inputRules"></v-textarea>

                        <v-menu>
                            <v-text-field disabled :value="date" slot="activator" label="Date" prepend-icon="date_range"></v-text-field>
                            <!--<v-date-picker v-model="date"></v-date-picker>-->
                        </v-menu>
                        
                        <v-spacer></v-spacer>

                        <v-btn flat class="info mx-3 mt-3" @click="publish" :loading="loading">Save and Publish</v-btn>
                        <v-btn flat round style="border-radius:7px;" class="info mx-0 mt-3" @click="dialog = false">Cancel</v-btn>
                    </v-form>
                </v-card-text>
            </v-card>
             <v-card min width="725px" class="px-5">
                <v-card-title>
                    <h2>Preview</h2>
                </v-card-title>
                <v-card-text>
                    <h2>{{ editedTitle }}</h2>
                    <v-layout row justify-start align-start>
                        <v-flex class="caption grey--text">Written by {{ user }}</v-flex>
                        <v-flex class="caption grey--text">Published on {{ date }}</v-flex>
                    </v-layout>
                    <br>
                    <p>{{ editedContent }}</p>
                </v-card-text>
            </v-card>
            </v-layout>
    </v-dialog>
</template>

<script>
//import axios from 'axios'
import db from '@/fb'
export default {
    props: ['post'],
    data() {
        return {
            // load the data from the post array via props
            editedTitle: this.post.title,
            editedContent: this.post.content,
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
            postId: this.post.id,
            // hard-coded user - change later
            user: 'Tom'
        }
    },
    methods: {
        publish() {
            if(this.$refs.form.validate()) {
                //use this when we actually put it in the database to show a loading sign
                this.loading = true; 
               
                const update = {}
                if (this.editedTitle) {
                    update.title = this.editedTitle
                    update.date  = this.date
                }
                if (this.editedContent) {
                    update.content = this.editedContent
                    update.date  = this.date
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
            }
        }
        /*
        cancel() {
            this.editedtitle = this.posts.title
            this.editedcontent = this.posts.content
            this.date = this.posts.date
        }*/
    },
    created() {
        db.collection('posts').get().then(snapshot => {
            snapshot.docs.forEach(doc => {
                this.posts.push(doc.data())
            })
        })
    }
    
    /*
    created: function() {
        this.fetchItems();
    }*/
}
</script>