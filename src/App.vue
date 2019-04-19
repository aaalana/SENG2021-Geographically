<template>
  <v-app>
    <v-content>
      <router-view>
        <div id="nav">
          <router-link to="/">Home</router-link> 
          <router-link to="/contactUs">Contact us</router-link>
        </div>
      </router-view>
    </v-content>
  </v-app>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'App',
}
</script>
