<template>
  <div class="dasboard">
    <v-content class="dblayout">
    <link href='https://fonts.googleapis.com/css?family=Quicksand' rel='stylesheet'>
      <v-layout row>
        <v-flex xs12>
          <h1 style="font-family:Quicksand;padding:30px;font-size:30px">Map Mode</h1>
          <div id = dMap>
          <router-link to="/map">
          <img id = "dMap" src="../assets/dMap.png" style="padding:30px" height="522px" width="900px">
          </router-link>
          </div>
        </v-flex>
        <v-flex xs12>
          <h2 style="font-family:Quicksand;padding-bottom:30px;padding-top:30px;font-size:30px">Nearby Attractions</h2>
          <p style="font-size:20px;padding:5px">Royal Botanical Gardens</p>
          <img id = "yeet" src="../assets/royalbg.png" style="padding:5px" height="232px" width="309px">
          <p style="font-size:20px;padding:5px">Anzac Memorial</p>
          <img id = "yeet" src= "../assets/anzac.png" style="padding:5px" height="232px" width="309px">
        </v-flex>
      </v-layout> 

      <v-layout row align-content-center mb-5>
        <v-flex xs12>
          <h3 style="font-family:Quicksand;padding:30px;font-size:30px">Road Trip!</h3>
            <v-carousel style="width:90%">
              <v-carousel-item
                v-for="(item,i) in items"
                :key="i"
                :src="item['src']"
              ></v-carousel-item>
            </v-carousel>
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
