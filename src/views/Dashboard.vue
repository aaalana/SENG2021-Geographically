<template>
  <div class="dasboard">
    <v-container class="dblayout">

      <v-layout row>
        <v-flex xs12>
          <h1 style="font-family:Quicksand;padding:30px;font-size:30px">Map Mode</h1>
          <div id = dMap>
          <router-link to="/map">
            <img id = "dMap" src="../assets/dMap.png" style="padding:30px" height="522px" width="1000px">
          </router-link>
          </div>
        </v-flex>
        <v-flex xs12>
          <h2 style="font-family:Quicksand;padding:30px;font-size:30px">Nearby Attractions</h2>
          <p style="font-size:20px;padding:5px">Royal Botanical Gardens</p>
          <img id = "yeet" src="../assets/royalbg.png" style="padding:5px" height="232px" width="309px">
          <p style="font-size:20px;padding:5px">Anzac Memorial</p>
          <img id = "yeet" src="../assets/anzac.png" style="padding:5px" height="232px" width="309px">
        </v-flex>
      </v-layout>

      <v-layout row>
        <v-flex xs12>
          <h3 style="font-family:Quicksand;padding:30px;font-size:30px">Road Trip!</h3>
          <template>
            <v-carousel>
              <v-carousel-item
                v-for="(item,i) in items"
                :key="i"
                :src="item.src"
              ></v-carousel-item>
            </v-carousel>
          </template>
        </v-flex>
      </v-layout>

    </v-container>


    <ContactUs />
    <Menu />
    <Footer />
  </div>
</template>

<script>
import Footer from '@/components/Footer.vue'
import Menu from '@/components/Menu.vue'

export default {
  name: 'dashboard',
  components: {
    Footer,
    Menu
  },
  data () {
    return {
      items: [
        {
          src: 'https://i.imgur.com/Udpl0Mu.jpg'
        },
        {
          src: 'https://i.imgur.com/GAnTyFJ.jpg'
        },
        {
          src: 'https://cdn.vuetifyjs.com/images/carousel/bird.jpg'
        },
        {
          src: 'https://cdn.vuetifyjs.com/images/carousel/planet.jpg'
        }
      ]
    }
  }
}

</script>
