<template>
    <div class="blog">
    <v-content>
        <link href='https://fonts.googleapis.com/css?family=Quicksand' rel='stylesheet'>
        <v-flex mb-4>
        <h1 class="display-2 font-weight-bold mb-3">
            <br>My Blog
        </h1>
        <h1 class="display-1 font-weight-bold mb-3">
            <br>Posts
        </h1>
        <p class="subheading font-weight-regular">
          For help and collaboration with other Vuetify developers,
          <br>please join our online
          <a href="https://community.vuetifyjs.com" target="_blank">Discord Community</a>
        </p>
      </v-flex>
      
        <v-card width="344">
        <v-layout row wrap>
            <v-card-title>
                <v-icon large left>description</v-icon>
                <span class="headline">me</span>
            </v-card-title>
        </v-layout>
        <v-layout row justify-center align-center>
         <div class="text-xs-center">
            <v-btn color="info" class="font-weight-medium" dark>VIEW BLOG POST</v-btn>
        </div>
        </v-layout>
        </v-card>

    </v-content>
    <Menu />
    </div>
</template>

<script>
// @ is an alias to /src
import Menu from '@/components/Menu.vue'

export default {
  name: 'blog',
  components: {
    Menu
  }
}
</script>