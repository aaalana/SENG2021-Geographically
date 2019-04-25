<template>
  
  <v-app>
    <div>
      <v-container fluid>
      <v-layout row wrap>
        <v-flex d-flex xs1 sm1 md1>
          <sidebar />
        </v-flex>
        <v-flex d-flex xs6 sm6 md6 order-lg2>
          <v-layout column>
            <link href='https://fonts.googleapis.com/css?family=Quicksand' rel='stylesheet'>
            <h1 style="font-family:Quicksand; font-size:30px;">Plan</h1> 
            <v-flex d-flex xs4 sm4 md4>   
              <timeline :parentData="myData" v-on:childToParent2="onChildClick2" v-on:childToParent="onChildClick"/>
            </v-flex>
            <v-flex d-flex xs12 sm12 md12 order-lg2>
              <v-layout row wrap>
                <randomMap />
                <v-divider></v-divider>
              </v-layout>
            </v-flex>
          </v-layout>
        </v-flex>
        <v-flex d-flex xs4 offset-xs1 offset-sm1 offset-md1 order-lg3>
          <v-layout column>
            <v-flex d-flex xs4></v-flex>
            <v-flex d-flex xs4 sm4 md4 order-lg2>
              <v-layout row wrap>
                <v-flex xs5>
                  <selectDate />
                </v-flex>
                <v-flex xs1></v-flex>
                <v-flex xs5>
                  <selectTime @inputData="getTime" />
                </v-flex>
              </v-layout>
            </v-flex>
            <v-flex d-flex xs6 sm6 md6 order-lg3>
              <v-layout row wrap>
                <v-flex xs7></v-flex>
                <v-flex xs5 order-lg2>
                  <v-btn flat @click="saveTrip()" ><v-icon>save</v-icon>Save trip</v-btn>
                </v-flex>
              </v-layout>
            </v-flex>
            <v-flex d-flex xs8 sm8 md8 order-lg4>
              <p style="font-family:Quicksand; font-size:15px;">
                {{arrtime}} {{loc}}
                <br>
                  {{msg["start"]}} TO {{msg["end"]}}
                <v-divider></v-divider> 
                <br>
                LENGTH OF TRIP<br> {{msg["dis"]}}
                <br>
                APPROXIMATE TRIP TIME<br> {{msg["time"]}}
                <br>
                WEATHER<br>
                {{weather}} {{temp}} degrees
                <!--11&#0176;C--><br>
                MY TRIP PLAYLIST<br>
                <router-link :to="{ name: 'playlists', params: { endLoc } }">
                  Get a playlist
                </router-link>
                <br>
                <v-divider></v-divider> 
                <img :src=photo class=”cropimg”>
                <br>
                {{summary}}
              </p>
            </v-flex>
          </v-layout>
        </v-flex>
      </v-layout>
      </v-container>
    </div>
    <Footer />
  </v-app>
</template>

<script>
  import sidebar from '@/components/sidebar.vue'
  import timeline from '@/components/timeline.vue'
  import selectDate from '@/components/selectDate.vue'
  import selectTime from '@/components/selectTime.vue'
  import randomMap from '@/components/randomMap.vue'
  import axios from 'axios';
  import Footer from '@/components/Footer.vue'
  import db from '@/fb'
  //import VueGoogleAutocomplete from 'vue-google-autocomplete'

  export default {
    name: 'tripPlanning',
    props: ["loc"],
    components: {
      sidebar,
      timeline,
      selectDate,
      selectTime,
      randomMap,
      Footer,
    },
    data() {
      return {
        msg: [],
        summary:[],
        photo: [],
        deptime: '',
        arrtime: '',
        address:'',
        weather:'24',
        temp:'',
        endLoc: '',
        fromChild: '',
        fromChild2: '',
      };
    },

     mounted() {
            // To demonstrate functionality of exposed component functions
            // Here we make focus on the user input
            this.$refs.address.focus();
            if (this.loc) {
              this.msg["end"] = this.loc    
            }
        },
    methods: {
      onChildClick (value) {
      this.fromChild = value
      },
      onChildClick2 (value) {
      this.fromChild2 = value
      },
      getTrip() {
        const path = 'http://localhost:5000/trips';
        axios.get(path)
          .then((res) => {
            this.msg = res.data; 
            this.endLoc = res.data["end"];
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
          });
      },
      getTripSummary() {
        const path = 'http://localhost:5000/trips/summary';
        axios.get(path)
          .then((res) => {
            this.summary = res.data;
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
          });
      },
      getTripPhoto() {
        const path = 'http://localhost:5000/trips/photo';
        axios.get(path)
          .then((res) => {
            this.photo = res.data;
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
          });
      },
      getTripWeather() {
        const path = 'http://localhost:5000/trips/weather';
        axios.get(path)
          .then((res) => {
            this.weather = res.data["forecasts"]["weather"]["days"][0]["entries"][0]["precis"];
            this.temp = res.data["forecasts"]["weather"]["days"][0]["entries"][0]["max"];
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
          });
      },
      getTime(time) {
        this.deptime = time
        this.arrtime = time + this.msg["timesec"]
        alert(this.msg["timesec"])
      },
      getAddressData: function (addressData) {
                this.address = addressData;
      },
      reloadPage(){
        window.location.reload()
      },

      saveTrip() {
        
        const newTrip = {
            start: this.msg["start"],
            end: this.msg["end"]
        }
        
        // add to firebase
        db.collection('trips').add(newTrip).then(() => {
            alert('trip added successfully');
        })
        .catch(error => {
            console.log(error);
        })
      },
  },
      created() {
        this.getTripWeather();
        this.getTripPhoto();
        this.getTrip();
        this.getTripSummary();
        this.getLocation();
      },

}
</script>

<style>
  body {
    background-color: white;
  }

  h1 {
    color: black;
    text-align: left;
    font-family: Arial, Helvetica, sans-serif;
  }

  p {
    font-family: Arial, Helvetica, sans-serif;
    font-size: 11px;
  }
  .cropimg {
    width: 200px;
    height: 150px;
    overflow: hidden;

}
</style>
