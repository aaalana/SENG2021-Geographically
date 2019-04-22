<template>
    <v-container fill-height>
      <NavBar />
      <v-layout row wrap align-center>
        <v-flex class="text-xs-center">
          <div class="font-weight-bold display-2" style="color:#424242">FAQs</div><br>
          <div class="title" style="color:#424242">
            <v-expansion-panel class="my-5" style="line-height:20px; font-family: Quicksand;">
              <v-expansion-panel-content>
              <template v-slot:header>
              <div class="font-weight-bold">What is Geographically?</div>
              </template>
              <v-card>
              <v-card-text class="grey lighten-3">
                <div class="subheading">Geographically is a simple web app which combines many features that would be useful when going on your trip. This includes: <br>
                - a map feature which allows you to search locations and learn about them more.<br>
                - a trip planner which provides trip directions, weather details and the duration of your trip<br>
                - a trip playlist which allows you to generate a playlist via spotify<br>
                - a blog so you can record how you felt about the places you have visited
                </div>
            </v-card-text>
              </v-card>
              </v-expansion-panel-content>

              <v-expansion-panel-content>
              <template v-slot:header>
              <div class="font-weight-bold">When was Geographically made?</div>
              </template>
              <v-card>
              <v-card-text class="grey lighten-3">
                <div class="subheading">March 2019 - April 2019</div>
              </v-card-text>
              </v-card>
              </v-expansion-panel-content>

              <v-expansion-panel-content>
              <template v-slot:header>
              <div class="font-weight-bold">What APIs does Geographically use?</div>
              </template>
              <v-card>
              <v-card-text class="grey lighten-3">
                <div class="subheading">Several APIs are used including Google maps, Wikipedia, Spotify and WillyWeather.</div>
              </v-card-text>
              </v-card>
              </v-expansion-panel-content>

              <v-expansion-panel-content>
              <template v-slot:header>
              <div class="font-weight-bold">How do I write to my trip blog?</div>
              </template>
              <v-card>
              <v-card-text class="grey lighten-3">
                <div class="subheading">After logging in, click on the blog icon from your sidebar. Here, you will be directed to your blog page. Click on 'make a new blog post' to get started in writing to your blog. Remember to click 'save and publish' when you're done to save your blog post.</div>
              </v-card-text>
              </v-card>
              </v-expansion-panel-content>
              
              <v-expansion-panel-content>
              <template v-slot:header>
              <div class="font-weight-bold">How do I plan a trip?</div>
              </template>
              <v-card>
              <v-card-text class="grey lighten-3">
                <div class="subheading">Click on the car icon from your sidebar and type in the location you want to visit. Geographically will then generate a route for you which you can save and view from your profile page. If you can't decide on a location to visit, visit the dashboard page to find some recommendations. If you click on a location from your dashboard, Geographically will automatically generate a route for you on your trip planner.</div>
              </v-card-text>
              </v-card>
              </v-expansion-panel-content>

              <v-expansion-panel-content>
              <template v-slot:header>
              <div class="font-weight-bold">How do I plan a trip?</div>
              </template>
              <v-card>
              <v-card-text class="grey lighten-3">
                <div class="subheading">Click on the car icon from your sidebar and type in the location you want to visit. Geographically will then generate a route for you which you can save and view from your profile page. If you can't decide on a location to visit, visit the dashboard page to find some recommendations.</div>
              </v-card-text>
              </v-card>
              </v-expansion-panel-content>
              
              <v-expansion-panel-content>
              <template v-slot:header>
              <div class="font-weight-bold">How do I generate a playlist for my trip?</div>
              </template>
              <v-card>
              <v-card-text class="grey lighten-3">
                <div class="subheading">Click on the music icon from your sidebar. Here, when you click 'generate your playlist!', Geographically will provide you a random trip playlist that you can save to your trip plan. Alternatively, when you are planning your trip on your 'Plan' page, you can also generate new playlist there when clicking on the button under 'My Trip Playlist'.</div>
              </v-card-text>
              </v-card>
              </v-expansion-panel-content>
            </v-expansion-panel>
          </div>
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
