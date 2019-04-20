<template>
  <div class="dasboard">
    <v-content class="dblayout">
    <link href='https://fonts.googleapis.com/css?family=Quicksand' rel='stylesheet'>
      <v-layout row>
        <v-flex xs12>
          <v-card>
          <h1 style="font-family:Quicksand;padding:30px;font-size:30px">Map Mode</h1>
          <div id = dMap>
          <router-link to="/map">
            <img id = "dMap" src="../assets/dMap.png" style="padding:30px" height="417px" width="800px">
          </router-link>
          </div>
          </v-card>
        </v-flex>
        <div style="width:20px"></div>
        <v-flex xs12>
          <v-card>
          <h2 style="font-family:Quicksand;padding:30px;font-size:30px">Nearby Attractions</h2>
          <div style="padding:20px">
            <p style="font-family:Quicksand;font-size:20px;text-align:center">Royal Botanical Gardens</p>
            <img id = "yeet" src="../assets/royalbg.png" style=";display:block;margin:0 auto" height="186px" width="247px">
          </div>
          <div style="padding:20px">
            <p style="font-family:Quicksand;font-size:20px;text-align:center" >Anzac Memorial</p>
            <img id = "yeet" src="../assets/anzac.png" style="display:block;margin:0 auto" height="186px" width="247px">
          </div>
          </v-card>
        </v-flex>
      </v-layout>

      <v-layout class="mt-5" row>
        <v-flex xs12>
          <v-card>
          <h3 style="font-family:Quicksand;padding:30px;font-size:30px">Road Trip!</h3>
            <v-carousel style="width:90%">
              <v-carousel-item
                v-for="(item,i) in items"
                :key="i"
                :src="item['src']"
              ></v-carousel-item>
            </v-carousel>
          </template>
          </v-card>
        </v-flex>
      </v-layout>
      <br><br>
    </v-content>
    <Menu />
    <Footer />
  </div>
</template>

<script>
import Footer from '@/components/Footer.vue'
import Menu from '@/components/Menu.vue'
import axios from 'axios';

export default {
  name: 'dashboard',
  components: {
    Footer,
    Menu
  },
  data () {
    return {
      items: [],
    }
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:5000/recommendation';
      axios.get(path)
        .then((res) => {
          this.items = res.data;
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


      }

  },
  created() {
    this.getMessage();
    this.getTripPhoto()
  },


}

</script>
