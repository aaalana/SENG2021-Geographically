<template>
  <v-app>
    <div>
      <v-container fluid>
        <v-layout row wrap>
          <v-flex xs1 sm1 md1>
            <sidebar />
          </v-flex>
          <v-flex>
            <v-card flat width=400px>
              <link href='https://fonts.googleapis.com/css?family=Quicksand' rel='stylesheet'>
              <v-card-title style="font-family:Quicksand; font-size:30px;"> Edit Profile </v-card-title>
              <v-divider></v-divider>
              <v-form>
                <v-text-field
                 style="font-family:Quicksand; font-size:15px;"
                 solo
                 label="New name">
                </v-text-field>
                <v-spacer></v-spacer>
                <v-text-field
                 style="font-family:Quicksand; font-size:15px;"
                 solo
                 label="New address">
                </v-text-field>
                <v-btn align-center color="info">Edit Details</v-btn>
              </v-form>
            </v-card>
          </v-flex>

        </v-layout>
      </v-container>
    </div>
    <Footer />
  </v-app>
</template>

<script>
  import sidebar from '@/components/sidebar.vue'
  import Footer from '@/components/Footer.vue'

  export default {
    name: 'App',
    return() {
      data: {
        message: false
      }
    },
    components: {
      sidebar,
      Footer
    }
}
</script>
