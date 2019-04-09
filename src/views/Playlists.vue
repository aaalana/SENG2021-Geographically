<template>
  <div class = "playlistpage">
    <v-container>
    <v-layout row>
    <link href='https://fonts.googleapis.com/css?family=Quicksand' rel='stylesheet'>
      <v-flex xs12>
        <h1 style="font-family:Quicksand;padding:30px;font-size:30px">Your Trip</h1>
        <p style="font-size:20px;padding:5px">Katoomba from 12/12/18</p>
        <img id = "playlisticon" src="../assets/playlisticon.png" style="padding:30px" height="522px" width="522px">
        <v-btn class="mt-5" id="start" round color="info" med>Generate Your Playlist!</v-btn>
      </v-flex>
      <v-flex xs12>
        <h2 style="font-family:Quicksand;padding:30px;font-size:30px">Your Playlist</h2>
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

export default {
  name: 'playlists',
  components: {
    Footer,
    Menu
  }
}

</script>
