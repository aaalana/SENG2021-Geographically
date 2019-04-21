<template>
  <div class = "playlistpage">
    <v-container>
    <v-layout row>
    <link href='https://fonts.googleapis.com/css?family=Quicksand' rel='stylesheet'>
      <v-flex xs12>
        <h1 style="font-family:Quicksand;padding:30px;font-size:30px">Your Trip</h1>
        <p style="font-size:20px;padding:5px">Katoomba from dd/mm/yy</p>
        <img id = "playlisticon" src="../assets/playlisticon.png" style="padding:30px" height="522px" width="522px">
        <v-btn class="mt-5" id="start" round color="info" med>Generate Your Playlist!</v-btn>
      </v-flex>
      <v-flex xs12>
        <h2 style="font-family:Quicksand;padding:30px;font-size:30px">Your Playlist Recommendations</h2>
        <li v-for="playlist in playlists">
          <a v-bind:href="playlist['external_urls']['spotify']" >{{playlist['name']}}</a>
        </li>
      </v-flex>
    </v-layout>
    </v-container>
    <ContactUs />
    <Menu />
    <Footer />
  </div>
</template>

<script>
import Footer from '@/components/Footer.vue'
import Menu from '@/components/Menu.vue'
import axios from 'axios'

export default {
  name: 'playlists',
  components: {
    Footer,
    Menu
  },
  data() {
        return {
            result: [],
            playlists: ""
        };
    }, 
  methods: {
    getPlaylist() {
      const path = 'http://localhost:5000/trips/music';
      axios.get(path)
        .then((res) => {
          this.result = res.data;
          this.playlists= res.data['playlists']['items']
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
        this.getPlaylist();
      }
}



</script>
