<template>
  <v-navigation-drawer
    v-model="drawer"
    :mini-variant.sync="mini"
    hide-overlay
    stateless
    app
    dark
  >
    <v-toolbar flat class="transparent">
      <v-list class="pa-0">
        <v-list-tile avatar>
          <v-list-item-avatar>
            <img style="padding-right: 15px;" alt="logo" src="../assets/mapLogo.png" height=30px>
          </v-list-item-avatar>

          <v-list-tile-content>
            <v-list-tile-title>Geographically</v-list-tile-title>
          </v-list-tile-content>

          <v-list-tile-action>
              <v-btn icon @click.stop="mini = !mini">
                <v-icon>chevron_left</v-icon>
              </v-btn>
          </v-list-tile-action>
        </v-list-tile>
      </v-list>
    </v-toolbar>

    <v-list class="pt-0">
      <v-divider></v-divider>

      <v-list-tile
        v-for="item in items"
        :key="item.title"
        @click=""
        router :to="item.route"
      >
        <v-list-tile-action>
          <v-icon>{{ item.icon }}</v-icon>
        </v-list-tile-action>

        <v-list-tile-content>
          <v-list-tile-title>{{ item.title }}</v-list-tile-title>
        </v-list-tile-content>
        
      </v-list-tile>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
  export default {
    data () {
      return {
        drawer: true,
        items: [
          { title: 'Dashboard', icon: 'dashboard', route: '/dashboard'},
          { title: 'My Profile', icon: 'account_circle', route: '/myProfile'},
          { title: 'Map Mode', icon: 'map', route: '/map'},
          { title: 'Trip Planning', icon: 'directions_car', route: '/tripPlanning'},
          { title: 'Playlists', icon: 'queue_music', route: '/playlists'},
          { title: 'My Blog', icon: 'library_books', route: '/myBlog'},
          { title: 'Log Out', icon: 'subdirectory_arrow_left', route: '/'}
        ],
        mini: true
      }
    }
  }
</script>
