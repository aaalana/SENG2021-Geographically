<template>
  <nav>
    <v-toolbar app right dark>
      <link href='https://fonts.googleapis.com/css?family=Quicksand' rel='stylesheet'>
      <a href="/"><img alt="logo" src="../assets/mapLogo.png" height=30px></a>
      <v-toolbar-title class="headline text">
        <span style= "font-family:Quicksand" class="font-weight-regular">Geographically</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
        <template>
          <v-layout row justify-center style="width:10px;height:10px;">
            <v-dialog v-model="dialog" dark persistent max-width="600px">
              <template v-slot:activator="{ on }">
                <v-btn color="normal" style= "font-family:Quicksand" border-radius=0px flat dark right v-on="on">Sign Up</v-btn>
              </template>
              <v-card>
                <v-card-title>
                  <span class="headline" colour=white >Sign Up</span>
                </v-card-title>
                <v-card-text>
                  <v-container grid-list-md>
                    <v-layout wrap>
                      <v-flex xs12>
                        <v-text-field label="Username*" required></v-text-field>
                      </v-flex>
                      <v-flex xs12 sm6 md4>
                        <v-text-field label="First Name*" required></v-text-field>
                      </v-flex>
                      <v-flex xs12 sm6 md4>
                        <v-text-field
                          label="Last name*"
                          hint="example of persistent helper text"
                          persistent-hint
                          required
                        ></v-text-field>
                      </v-flex>
                      <v-flex xs12>
                        <v-text-field label="Email*" required></v-text-field>
                      </v-flex>
                      <v-flex xs12>
                        <v-text-field label="Mobile"></v-text-field>
                      </v-flex>
                      <v-flex xs12>
                        <v-text-field label="Password*" type="password" required></v-text-field>
                      </v-flex>
                    </v-layout>
                  </v-container>
                  <small>*indicates required field</small>
                </v-card-text>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn color="blue darken-1" style="min-width:100px;min-height:50px;" flat @click="dialog=false">Close</v-btn>
                  <v-btn color="blue darken-1" style="min-width:100px;min-height:50px;" flat @click="dialog=false">Submit</v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </v-layout>
        </template>
        <template>
          <v-layout row justify-center style="width:10px;height:10px;">
            <v-dialog v-model="dialog2" dark persistent max-width="600px">
              <template v-slot:activator="{ on }">
                <v-btn color="normal" style= "font-family:Quicksand" flat dark v-on="on">Login</v-btn>
              </template>
              <v-card>
                <v-card-title>
                  <span class="headline">Login</span>
                </v-card-title>
                <v-card-text>
                  <v-container grid-list-md>
                    <v-layout wrap>
                      <v-flex xs12>
                        <v-text-field label="Username*" required></v-text-field>
                      </v-flex>
                      <v-flex xs12>
                        <v-text-field label="Password*" type="password" required></v-text-field>
                      </v-flex>
                    </v-layout>
                  </v-container>
                  <small>*indicates required field</small>
                </v-card-text>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn color="blue darken-1" style="min-width:100px;min-height:50px;" flat @click="dialog2=false">Close</v-btn>
                  <router-link to="/dashboard">
                    <v-btn color="blue darken-1" style="min-width:100px;min-height:50px;" flat @click="dialog2=false">Login</v-btn>
                  </router-link>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </v-layout>
        </template>
    </v-toolbar>
  </nav>
</template>

<script>
  export default {
    data: () => ({
      dialog: false,
      dialog2: false
    })
  }
</script>
