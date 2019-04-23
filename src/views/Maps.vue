<template>
  <div>
    <div class="mapouter">
      <v-card>
      <v-content>
      <v-layout row wrap>
        <link href='https://fonts.googleapis.com/css?family=Quicksand' rel='stylesheet'>
        <v-flex>
          <br><v-card-title class="display-1" style="font-family: Quicksand">Map Mode</v-card-title>
        </v-flex>
        <v-spacer></v-spacer>
        <v-flex mt-4 mr-4>
          <v-form @submit="submit"
          onSubmit="return false;">
            <v-text-field
             style="font-family:Quicksand; font-size:15px;"
             label="Search a location"
             v-model="location"
             prepend-inner-icon="place"
             ></v-text-field>
          </v-form>
        </v-flex>
      </v-layout>
      </v-content>
      </v-card>
      <div class="gmap_canvas">
        <iframe
          id="gmap_canvas"
          width="100%"
          height="100%"
          :src="url"
          frameborder="0"
          scrolling="no"
          marginheight="0"
          marginwidth="0"
        />
      </div>
    </div>
    <Menu />
  </div>
</template>

<script>
// @ is an alias to /src
import Menu from '@/components/Menu.vue'
import axios from 'axios'

export default {
  name: 'map',
  components: {
    Menu
  },
  data() {
    return {
      location: "",
      url: "https://maps.google.com/maps?q=&t=&z=13&ie=UTF8&iwloc=&output=embed",
    };
  },
  methods: {
    submit:function() {
      this.url = "https://maps.google.com/maps?q="+this.location+"&t=&z=13&ie=UTF8&iwloc=&output=embed"
    },
  }
};
</script>

<style>
.mapouter {
  text-align:right;
  height:100%;
  width:100%;
  position: absolute;
}
.gmap_canvas {
  overflow:hidden;
  background:none!important;
  height:100%;
  width:100%;
}
</style>
