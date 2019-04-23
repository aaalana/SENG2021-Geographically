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
              > My Profile <router-link to="/editProfile"><v-btn icon left><v-icon>event</v-icon></v-btn></router-link>
              </v-card-title>
              <v-divider></v-divider>
              <v-card-text style="font-family:Quicksand; font-size:15px;">
                <h4 style="font-family:Quicksand; font-size:20px;">John</h4>
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
            <v-card flat width=600px>
              <link href='https://fonts.googleapis.com/css?family=Quicksand' rel='stylesheet'>
              <v-layout row wrap>
              <v-card-title
              style="font-family:Quicksand; font-size:30px;"
              > My trips <v-btn flat left to="/tripPlanning"><v-icon style="padding-right:5px;">control_point</v-icon>Start planning</v-btn>
              </v-card-title> 
              </v-layout>
              <v-divider></v-divider>
              <v-card-text style="font-family:Quicksand; font-size:15px;">
                <v-card class="my-3" v-for="trip in trips" style="font-family:Quicksand; font-size:15px;" width=575px>
                  <v-icon medium>navigation</v-icon>{{trip.start}} TO {{trip.end}}
                  <v-spacer></v-spacer>
                  <v-layout align-end>
                  <v-btn icon left  @click="deleteTrip(trip)"><v-icon>delete</v-icon></v-btn>
                    <v-flex xs3></v-flex>
                    <v-flex xs2 style="padding: 10px;">
                  <router-link style="text-decoration:none;" :to="{ name: 'tripPlanning', params: {trip} }">
                  <v-btn style="border-radius:7px;" align-end color="info" v-on:click="sendInfo(trip.start,trip.end)">View trip details</v-btn>
                  </router-link>
                    </v-flex>
                  <v-spacer></v-spacer>
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
  import axios from 'axios'

  export default {
    name: 'App',
      data() {
        return {
        message: false,
        trips: [],
        databaseNotEmpty: false, // looks at when firebase finishes putting data into the posts array to control when the loading sign shows
        empty: false, // check if there are any blog posts
        currstart: "",
        currend: "",
        posts: [],
      }
    },
    components: {
      sidebar,
      Footer
    },
    methods: {
      sendInfo(start, end) {
        const path = 'http://localhost:5000/location';
        this.currstart = start;
        this.currend = end;
        alert(this.currend)
        axios.post(path,{
            start: this.currstart,
            end: this.currend,
        }
        )
        .then(() => {
          this.$emit('childToParent', origin)
            this.$emit('childToParent2', dest)
        })
        .catch((err) => {
          console.log(err)
        });
      },
      getCurrLocation(start, end) {
        this.currstart = start;
        this.currend = end;
      },
      getTrip(start,end) {
        this.getCurrLocation(start,end);
        alert(this.currstart)
        this.sendInfo();
      
      },
      deleteTrip(trip) {
            // delete post from the database
            db.collection('trips').doc(trip.id).delete().then(function() {
                console.log("Trip successfully deleted!");
            }).catch(function(error) {
                console.error("Error removing trip: ", error);
            });
            
            // delete post from the post array that shows the posts list on the webpage
            let index
            for (let i = 0; i < this.trips.length; i++) {
                if (trip.id === this.trips[i].id) {
                    index = i
                    break
                }
            }
            this.trips.splice(index, 1)

            // trigger empty blog posts message 
            if (this.trips.length === 0) {
                this.empty = true;
            }
        },
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
      var tripsRef = db.collection('trips');
      var allTrips = tripsRef.get()
          
        .then(snapshot => {
          snapshot.forEach(doc => {
            this.trips.push({id: doc.id, ...doc.data()});
            //alert(doc.id, '=>', doc.data());
          });
        })
        .catch(err => {
          console.log('Error getting documents', err);
        });
        
    },
}
</script>


