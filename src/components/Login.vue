 <template>
  <form id="signup-form">
    <v-btn color="normal" style= "font-family:Quicksand" border-radius=0px flat dark right @click="dialog = true">Login</v-btn>
    <v-layout row justify-center style="width:10px;height:10px;">
    <v-dialog v-model="dialog" dark no-click-animation persistent max-width="600px">
  
    <v-card>
      <v-form ref="form">
      <v-card-title>
        <span class="headline" colour=white >Login</span>
      </v-card-title>

      <v-card-text>
        <v-container grid-list-md>
          <v-layout wrap>
              
            <v-flex xs12>
              <v-text-field v-model="email" :rules="inputRules" id="signup-email" label="Email*" required></v-text-field>
            </v-flex>

            <v-flex xs12>
              <v-text-field v-model="password" :rules="inputRules" id="signup-password" label="Password*" type="password" required></v-text-field>
            </v-flex>
            <small>*indicates required field</small>
          </v-layout>
        </v-container> 
      </v-card-text>   
      
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="blue darken-1" style="min-width:100px;min-height:50px;" flat @click="dialog=false">Close</v-btn>
        <v-btn id="submit" color="blue darken-1" style="min-width:100px;min-height:50px;" flat @click="login">Submit</v-btn>
      </v-card-actions>
      </v-form>
      </v-card>
      </v-dialog>
    </v-layout>
  </form>
</template>

<script>
import db from '@/fb'
import auth from '@/fb'
import firebase from 'firebase'

export default {
    data() { 
      return {
        user: '',
        email:'',
        password: '',
        dialog: false,
        inputRules: [
            v => v.trim() !== '' || 'You cannot leave this field empty'
        ],
      }
    },
    methods: {
        login: function(e) {
        if(this.$refs.form.validate()) {
            // fill this in
            this.dialog = false;
        }
      }
    }
}
</script>