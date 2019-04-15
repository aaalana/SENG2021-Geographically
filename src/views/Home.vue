<template>
  <div class="home" style="background-color:white;">
 
    <v-layout justify-center class="text-xs-center">
      <v-flex xs12 md1 id="markPosition">
        <v-img aspect-ratio="0.7" max-height="95" max-width="65" id="mark" :src="require('../assets/locationMark.png')"/>
      </v-flex>
    </v-layout>

    <v-layout justify-center class="text-xs-center">
      <v-flex xs12>
          <p class="title" id="intro"> Do you always struggle to plan your trip? No worries, <br> we got you covered. </p>
      </v-flex>
    </v-layout>
   

    <div id="resize">
      <img id="logo" src="../assets/introMap.png">
    </div>
    
    <v-layout justify-center>
    <v-flex class="text-xs-center">
      <v-btn id="start" round color="info" large>Try Geographically Today</v-btn>
    </v-flex>
    </v-layout>
   
    
    <v-content>
      <v-card flat>
        <v-card-text>
          <v-container fluid class="pa-0">
            <v-layout class="text-xs-center">
              <v-flex xs12>
                <link href='https://fonts.googleapis.com/css?family=Quicksand' rel='stylesheet'>
                <p style="font-family:Quicksand; font-size:50px;"><b>About Us</b></p><br>
                <p class="title" style="padding-bottom:80px;">Geographically is a simple and easy-to-use online trip planning tool that allows you to plan your own travel itineraries.</p>
              </v-flex>
            </v-layout>
            <v-layout row wrap justify-center class="text-xs-center">
              <v-flex xs4>
                <v-img aspect-ratio="1" :src="require('../assets/music.png')" height="100%" width="50%" style="opacity:0.4; margin: auto"/>
              </v-flex>
        
              <v-flex xs4>
                <v-img aspect-ratio="1" :src="require('../assets/history.png')" height="100%" width="50%" style="opacity:0.5; margin: auto"/>
              </v-flex>

              <v-flex xs4>
                <v-img aspect-ratio="1" :src="require('../assets/weather.png')" height="100%" width="50%" style="opacity:0.5; margin: auto"/>
              </v-flex>
            </v-layout>

            <v-layout row wrap justify-center class="text-xs-center" style="padding-bottom:20px;">
              <v-flex xs4>
                <br><p class="display-1" >Listen to our customised <br> trip playlist</p>
              </v-flex>
              <v-flex xs4>
                <br><p class="display-1">Learn about the history of<br> a location</p>
              </v-flex>
              <v-flex xs4>
                <br><p class="display-1">Get real-time data<br> on locations</p><br><br><br>
              </v-flex>
            </v-layout>

            <v-layout row justify-center wrap>
              <v-flex xs4>
                <v-img aspect-ratio="1" :src="require('../assets/map.png')"  height="100%" width="50%" style="opacity:0.4; margin: auto"/>
              </v-flex>

              <v-flex xs4>
                <v-img aspect-ratio="1" :src="require('../assets/rate.png')"  height="100%" width="50%" style="opacity:0.4; margin: auto"/>
              </v-flex>

              <v-flex xs4>
                <v-img aspect-ratio="1" :src="require('../assets/free.png')" height="100%" width="50%" style="opacity:0.4; margin: auto"/>
              </v-flex>

            </v-layout>
             <v-layout row wrap justify-center class="text-xs-center" style="padding-bottom:20px;">
              <v-flex xs4>
                <br><p class="display-1">Find routes to nearby <br> hotels and tourist<br> attractions</p><br><br><br>
              </v-flex>
              <v-flex xs4>
                <br><p class="display-1">Rate and review the<br>places you visit</p>
              </v-flex>
              <v-flex xs4>
                <br><p class="display-1">Feel free to use without<br>any service fees</p>
              </v-flex>
            </v-layout>
          </v-container>
        </v-card-text>
      </v-card>
    </v-content>
    <NavBar />
    <Footer />
  </div>
</template>

<script>
// @ is an alias to /src
import NavBar from '@/components/NavBar.vue'
import Footer from '@/components/Footer.vue'

export default {
  name: 'home',
  components: {
    NavBar,
    Footer
  }
}
</script>

<style>
#resize {
  width: 100%;
  overflow: hidden;
  height:800px;
  margin-top: -200px
}

#logo {
  width:100%;
}

#start {
  font-size: 27px;
  border-radius: 100px;
  min-width: 450px;
  min-height: 100px;
  position: relative;
  top: -60px;
  text-transform: none;
}

#intro {
  position: absolute;
  top: 420px;
  color: white;
  text-shadow: 1px 1px rgb(26, 26, 26);
}

#mark {
  top: 400px;
  left: 25%;
}

#intro {
  top: 520px;
  color: white;
  left: 35%;
  text-shadow: 1px 1px rgb(26, 26, 26);
}
</style>