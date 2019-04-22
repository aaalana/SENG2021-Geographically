<template>
    <v-container fill-height>
      <NavBar />
      <v-layout row wrap align-center>
        <v-flex class="text-xs-center">
          <div class="font-weight-bold display-2" style="color:#424242">Contact Us</div><br>
          <p class="title" style="color:#424242">Phone number: 0405 455 888</p>
          <p class="title" style="color:#424242">Email: TeamA@gmail.com</p>
          <p class="title" style="color:#424242">-Team A</p>
        </v-flex>
      </v-layout>
      <Footer />
    </v-container>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
import Footer from '@/components/Footer.vue'

export default {
  components: {
    NavBar,
    Footer
  }
}
</script>
