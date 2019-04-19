<template>
    <v-container fill-height>
      <NavBar />
      <v-layout row wrap align-center>
        <v-flex class="text-xs-center">
          <div class="font-weight-bold display-2" style="color:#424242">FAQs</div><br>
          <p class="title" style="color:#424242">No questions have been asked so far.</p>
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
