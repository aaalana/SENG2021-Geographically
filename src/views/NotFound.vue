<template>
    <v-container fill-height>
      <v-layout row wrap align-center>
        <v-flex class="text-xs-center">
          <img src="../assets/404.png" max height="250" style="opacity:0.7;">
          <br><br><div class="display-2" style="color:#424242">404 - Page not found</div><br>
          <p class="title" style="color:#424242">Sorry, we couldn't find the page you were looking for!</p>
          <v-btn class="info subheading" large round style="border-radius: 7px;" to="/">Visit Homepage</v-btn>
        </v-flex>
      </v-layout>
      <Footer />
    </v-container>
</template>

<script>
import Footer from '@/components/Footer.vue'

export default {
  components: {
    Footer
  }
}
</script>