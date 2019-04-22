<template>
  <v-app style="background-color: white;">
    <div class="mb-5">
      <v-container fluid>
        <v-layout row wrap>
          <v-flex xs1 sm1 md1>
            <sidebar />
          </v-flex>
          <v-flex>
            <v-card flat width=400px>
              <link href='https://fonts.googleapis.com/css?family=Quicksand' rel='stylesheet'>
              <v-card-title 
                style="font-family:Quicksand; font-size:30px;"
              > My Profile <v-btn icon left><v-icon>edit</v-icon></v-btn>
              </v-card-title> 
              <v-divider></v-divider>
              <v-card-text style="font-family:Quicksand; font-size:15px;">
                <h4 style="font-family:Quicksand; font-size:20px;">John Doe</h4>
                <v-icon medium>place</v-icon>1 Main Street, Sydney 2000
              </v-card-text>
            </v-card>
            <v-spacer></v-spacer>
            
            <v-card flat width=400px>
              <link href='https://fonts.googleapis.com/css?family=Quicksand' rel='stylesheet'>
              <v-card-title 
                style="font-family:Quicksand; font-size:30px;"
              > My Blogs <v-btn flat left to="blog"><v-icon style="padding-right:5px;">control_point</v-icon>Start writing</v-btn>
              </v-card-title> 

              <v-divider></v-divider>
              <v-card-text v-if="posts.length === 0"><div style="font-family:Quicksand;font-size:16px;">You have no blog posts.</div></v-card-text> 
                <v-card class="my-3" v-for="post in posts.slice(0, 3)" :key="post.id" style="font-family:Quicksand; font-size:18px;" width=400px>
                  <v-layout row wrap>
                  <v-icon large style="padding: 10px;">library_books</v-icon>
                  <v-flex><v-card-title style="word-wrap:break-word;" xs2 md2>{{ post.title }}</v-card-title></v-flex>
                  <v-spacer></v-spacer>
                  <v-flex align-content-end class="text-lg-right"><v-btn @click="deletePost(post)" style="margin-right:30px;" icon left><v-icon>delete</v-icon></v-btn></v-flex>
                  </v-layout>
                  
                  <v-card-actions class="justify-center"><v-btn :to ="'/blog/' + post.id" style="border-radius:7px;margin-bottom:10px;" color="info" large>View blog post</v-btn></v-card-actions>
                </v-card>
            </v-card>
          </v-flex>
          <v-flex>
            <v-card flat width=400px>
              <link href='https://fonts.googleapis.com/css?family=Quicksand' rel='stylesheet'>
              <v-card-title 
                style="font-family:Quicksand; font-size:30px;"
              > My Trips <v-btn icon left><v-icon>edit</v-icon></v-btn>
              </v-card-title> 
              <v-divider></v-divider>
              <v-card-text style="font-family:Quicksand; font-size:15px;">
                <v-card style="font-family:Quicksand; font-size:15px;" width=300px>
                  <v-icon medium>navigation</v-icon>Katoomba<v-btn icon left><v-icon>delete</v-icon></v-btn>
                  <v-spacer></v-spacer>
                  <v-layout align-center>
                    <v-flex xs3></v-flex>
                    <v-flex xs2>
                  <v-btn align-center color="info">View trip details</v-btn>
                    </v-flex>

                  </v-layout>
                </v-card>
                
              </v-card-text>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </div> 
    <Footer />
  </v-app>   
</template>

<script>
import sidebar from '@/components/sidebar.vue'
import Footer from '@/components/Footer.vue'
import db from '@/fb'

  export default {
    name: 'App',
      data() {
        return {
          message: false,
          posts: []
        }
    },
    components: {
      sidebar,
      Footer
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
                    this.posts.sort((a,b) => a.date > b.date ? -1 : 1);
                }
            })
      });
    }
}
</script>
