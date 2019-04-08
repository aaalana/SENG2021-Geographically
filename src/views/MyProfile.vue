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
              <v-card-title 
                style="font-family:Quicksand; font-size:30px;"
              > My Profile <v-btn icon left><v-icon>edit</v-icon></v-btn>
              </v-card-title> 
              <v-divider></v-divider>
              <v-card-text style="font-family:Quicksand; font-size:15px;">
                <h4 style="font-family:Quicksand; font-size:20px;">John Doe</h4>
                <v-icon medium>place</v-icon>1 Main Street, Sydney 2000
                
              </v-card-text>
            </v-card>
            <v-spacer></v-spacer>
            <v-card flat width=400px>
              <link href='https://fonts.googleapis.com/css?family=Quicksand' rel='stylesheet'>
              <v-card-title 
                style="font-family:Quicksand; font-size:30px;"
              > My Blogs <v-btn icon left><v-icon>edit</v-icon></v-btn>
              </v-card-title> 
              <v-divider></v-divider>
              <v-card-text style="font-family:Quicksand; font-size:15px;">
                <v-card style="font-family:Quicksand; font-size:15px;" width=300px>
                  <v-icon large>library_books</v-icon>My First Trip<v-btn icon left><v-icon>delete</v-icon></v-btn>
                  <v-spacer></v-spacer>
                  <v-layout align-center>
                    <v-flex xs3></v-flex>
                    <v-flex xs2>
                  <v-btn align-center color="info">View blog post</v-btn>
                    </v-flex>
                  </v-layout>
                </v-card>
              </v-card-text>
            </v-card>
          </v-flex>
          <v-flex>
            <v-card flat width=400px>
              <link href='https://fonts.googleapis.com/css?family=Quicksand' rel='stylesheet'>
              <v-card-title 
                style="font-family:Quicksand; font-size:30px;"
              > My Trips <v-btn icon left><v-icon>edit</v-icon></v-btn>
              </v-card-title> 
              <v-divider></v-divider>
              <v-card-text style="font-family:Quicksand; font-size:15px;">
                <v-card style="font-family:Quicksand; font-size:15px;" width=300px>
                  <v-icon medium>navigation</v-icon>Katoomba<v-btn icon left><v-icon>delete</v-icon></v-btn>
                  <v-spacer></v-spacer>
                  <v-layout align-center>
                    <v-flex xs3></v-flex>
                    <v-flex xs2>
                  <v-btn align-center color="info">View trip details</v-btn>
                    </v-flex>

                  </v-layout>
                </v-card>
                
              </v-card-text>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </div> 
  </v-app>   
</template>

<script>
  import sidebar from '@/components/sidebar.vue'
  export default {
    name: 'App',
    components: {
      sidebar
    }
}
</script>
