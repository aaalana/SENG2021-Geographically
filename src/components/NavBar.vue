<template>
  <nav>
    <v-toolbar app right dark>
      <link href='https://fonts.googleapis.com/css?family=Quicksand' rel='stylesheet'>
      <a href="/"><img alt="logo" src="../assets/mapLogo.png" height=30px></a>
      <v-toolbar-title class="headline text">
        <span style= "font-family:Quicksand" class="font-weight-regular">Geographically</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <Signup />
      <Login />
    </v-toolbar>

  </nav>
</template>

<script>
import Signup from '@/components/Signup.vue'
import Login from '@/components/Login.vue'
export default {
  components: {
      Signup,
      Login
  },
  data() {
    return {
      dialog2: false
    }
  }
}
</script>
