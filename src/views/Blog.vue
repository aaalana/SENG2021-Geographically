<template>
    <div class="blog">
        <nav>
            <v-snackbar v-model="snackbar" :timeout="4000" top color="info">
                <span>You have successfully published your blog post.</span>
                <v-btn flat color="white" @click="snackbar = false">Close</v-btn>
            </v-snackbar>
            <v-snackbar v-model="snackbar2" :timeout="4000" top color="info">
                <span>You have successfully updated your blog post.</span>
                <v-btn flat color="white" @click="snackbar2 = false">Close</v-btn>
            </v-snackbar>
            <v-snackbar v-model="snackbar3" :timeout="4000" top color="info">
                <span>There has been no changes made to save to your blog post.</span>
                <v-btn flat color="white" @click="snackbar3 = false">Close</v-btn>
            </v-snackbar>
        </nav>
        <v-content>
            <link href='https://fonts.googleapis.com/css?family=Quicksand' rel='stylesheet'>
            <v-flex mb-4>
                <h1 class="display-2 font-weight-bold mb-3">
                    <br>My Blog
                </h1>
                <h1 class="display-1 font-weight-bold mb-3">
                    <br>Posts
                </h1>
                <AddPost @blogPostAdded="snackbar = true" />
            </v-flex>

            <v-layout row wrap v-if="databaseNotEmpty === false && stopLoading === false">
                <v-flex xs12 class="text-xs-center">
                    <v-progress-circular indeterminate :size="70" :width="7" color="info"></v-progress-circular>
                </v-flex>
            </v-layout>

            <v-container class="my-5">
                <div v-if="empty === true"><h3 class= "font-weight-regular">You have no blog posts.</h3></div>
                <v-card v-for="post in posts" :key="post.id">
                    <v-layout row wrap :class="'pa-3 post ${post.status}'"> 
                        <v-flex xs6 md4>
                            <v-icon large left>description</v-icon>
                            <span class="headline">{{ post.title }}</span>
                        </v-flex>
                        <v-flex>
                            <v-card-actions>
                                <v-flex xs4 sm1 md4>
                                    <EditPost :post="post" @blogPostNotUpdated="snackbar3 = true" @blogPostUpdated="snackbar2 = true" @updateFrontEnd="updatePost(post)" />
                                </v-flex>
                                <v-flex xs4 sm1 md4>
                                    <v-btn @click="deletePost(post)" flat fab><v-icon>delete</v-icon></v-btn>
                                </v-flex>
                            </v-card-actions>
                        </v-flex>

                        <v-flex xs6 sm4 md2> <div class="caption grey--text">Date</div><div>{{ post.date }}</div></v-flex>
                            
                      <v-spacer></v-spacer>

                        <v-flex>
                            <v-card-actions class="text-xs-center">
                                <router-link :to ="/blog/ + post.id"><v-btn round style="border-radius:7px; width:250px; height:50px;" color="info" class="font-weight-regular subheading" dark>VIEW BLOG POST</v-btn></router-link>
                            </v-card-actions>
                        </v-flex>
                    </v-layout>
                </v-card>
            </v-container>
            <br><br><br>
        </v-content>
        <Menu />
        <Footer />
    </div>
</template>

<script>
// @ is an alias to /src
import Menu from '@/components/Menu.vue'
import AddPost from '@/components/AddPost.vue'
import EditPost from '@/components/EditPost.vue'
import db from '@/fb'
import Footer from '@/components/Footer.vue'

export default {
    name: 'blog',
    components: {
        Menu,
        AddPost,
        EditPost,
        Footer
    },
    data() {
        return {
            posts: [],
            snackbar: false, // make blogpost
            snackbar2: false, // update blogpost
            snackbar3: false, // cannot update blogpost
            databaseNotEmpty: false, // controls if the loading sign will start
            stopLoading: false,
            empty: false // check if there are any blog posts
        }
    },
    methods: {
        deletePost(post) {
            // delete post from the database
            db.collection('posts').doc(post.id).delete().then(function() {
                console.log("Post successfully deleted!");
            }).catch(function(error) {
                console.error("Error removing post: ", error);
            });
            
            // delete post from the post array that shows the posts list on the webpage
            let index
            for (let i = 0; i < this.posts.length; i++) {
                if (post.id === this.posts[i].id) {
                    index = i
                    break
                }
            }
            this.posts.splice(index, 1)

            if (this.posts.length === 0) {
                this.empty = true;
            }
        },
        updatePost(post) {
            // delete the post after the data has been pushed into the posts array via created()
            let index
            for (let i = 0; i < this.posts.length; i++) {
                if (post.id === this.posts[i].id) {
                    index = i
                    break
                }
            }
            this.posts.splice(index, 1)
        }
    },
    created() {
        db.collection('posts').onSnapshot(response => {
            const changes = response.docChanges();
            // loop through changes made in the firestore database and update them
            changes.forEach(change => {
                if  (change.type === 'added' || change.type === 'modified') {
                    // push to the posts array 
                    this.databaseNotEmpty = true,
                    this.empty = false,
                    this.posts.push({
                        ...change.doc.data(),
                        id: change.doc.id,
                    })
                }
            })
            if (this.databaseNotEmpty === false) {
                this.stopLoading = true;
                this.empty = true; 
            }
        })
        
    }
}
</script>

<style>
.post.published {
    border-left: 4px solid #3cd1c2;

}

.post.draft {
    border-left: 4px solid orange;
}
</style>