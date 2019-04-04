<template>
  <div class="home">
    <div id="resize">
    <img id="logo" src="../assets/introMap.png">
    </div>
    <div class="text-xs-center">
      <v-btn round color="info" large>Try Geographically Today</v-btn>
    </div>
    
    <div id="markPosition">
    <v-img id="mark" :src="require('../assets/locationMark.png')" height="95px" width="65px"/>
    </div>
    
    <p> Do you always struggle to plan your trip? No worries, we got you covered. </p>

    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <NavBar />
    <Footer />
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import NavBar from '@/components/NavBar.vue'
import Footer from '@/components/Footer.vue'

export default {
  name: 'home',
  components: {
    HelloWorld,
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

.v-btn {
  font-size: 27px;
  border-radius: 100px;
  min-width: 450px;
  min-height: 100px;
  position: relative;
  top: -60px;
  text-transform: none;
}

#mark {
  position: absolute;
  top: 300px;
  left: 47.9%;
}
</style>