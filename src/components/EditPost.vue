<template>
    <v-dialog persistent no-click-animation max width="100%" v-model="dialog">
        <v-btn flat fab slot="activator"><v-icon>edit</v-icon></v-btn>
            <v-layout row wrap>
            <v-card max width="50%" class="px-5">
                <v-card-title>
                    <h2>Edit Blog Post</h2>
                </v-card-title>
                <v-card-text>
                    <v-form ref="form">
                        <v-text-field label="Title" v-model="editedTitle" prepend-icon="folder" :rules="inputRules"></v-text-field>
                        <v-textarea label="Tell us about your trip" v-model="editedContent" prepend-icon="edit" :rules="inputRules"></v-textarea>
                        
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
                <v-card-title>
                    <h2>Preview</h2>
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
                    <div style="word-wrap: break-word;">{{ editedContent }}</div>
                </v-card-text>
            </v-card>
            </v-layout>
    </v-dialog>
</template>

<script>
//import axios from 'axios'
import db from '@/fb'
export default {
    // used to retrieve data found on blog.vue via :post
    props: ['post'],
    data() {
        return {
            // load the data from the post array via props
            editedTitle: this.post.title,
            editedContent: this.post.content,
            date: new Date(new Date().toString().split('GMT')[0]+' UTC').toISOString().split('T')[0],
            inputRules: [
                v => v.trim() !== '' || 'You cannot leave this empty'
            ],
            loading: false, // controls when the loading sign appears on the button
            dialog: false, // closes the add post window/pop up
            postId: this.post.id, // array of blog posts
            user: 'Tom',  // hard-coded user - change later
            rating: this.post.rating,
            rateLoc: this.post.locationRated,
            hasupdated: false
        }
    },
    methods: {
        publish() {
            if(this.$refs.form.validate() && this.madeChanges() === true) {
                //use this when we actually put it in the database to show a loading sign
                this.loading = true; 
               
                const update = {}
                // only update the changes made
                if (this.editedTitle !== this.post.title) {
                    update.title = this.editedTitle;
                    this.hasupdated = true;
                }

                if (this.editedContent !== this.post.content) {
                    update.content = this.editedContent;
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
            this.rateLoc= this.post.locationRated
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
        }
    }
}
</script>