<template>
    <v-dialog persistent no-click-animation max width="100%" v-model="dialog">
        <v-btn round style="border-radius:7px;" slot="activator" class="info">Add new post</v-btn>
            <v-layout row wrap>
            <v-card width="50%" class="px-5">
                <v-card-title>
                    <h2>Add Blog Post</h2>
                </v-card-title>
                <v-card-text>
                    <v-form ref="form">
                        <v-text-field label="Title" v-model="title" prepend-icon="folder" :rules="inputRules"></v-text-field>
                        <v-textarea label="Tell us about your trip" v-model="content" prepend-icon="edit" :rules="inputRules"></v-textarea>

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
                    <v-card-title primary-title>
                        <h2>Preview</h2>
                    </v-card-title>
                    <v-card-text>
                        <link href='https://fonts.googleapis.com/css?family=Quicksand' rel='stylesheet'>
                        <h2 style="font-family:Quicksand; word-wrap: break-word;">{{ title }}</h2>
                        <v-layout row justify-start align-start>
                            <v-flex pr-4 xs6 md6 class="caption grey--text" style="word-wrap: break-word;">Written by {{ user }}</v-flex>
                            <v-flex xs6 md6 class="caption grey--text" style="word-wrap: break-word;">Modified on {{ date }}</v-flex>
                        </v-layout>
                        <br>
                        <div style="word-wrap: break-word;">{{ content }}</div>
                    </v-card-text>
                </v-card>
            </v-layout>
    </v-dialog>
</template>

<script>
import db from '@/fb'
export default {
    data() {
        return {
            title: '',
            content: '',
            //date: new Date().toDateString() - puts date in words
            date: new Date(new Date().toString().split('GMT')[0]+' UTC').toISOString().split('T')[0],
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
            this.$refs.form.resetValidation();
        },
    }
}
</script>