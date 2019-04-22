 <template>
  <form id="login-form">
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
              <v-text-field v-model="email" :rules="inputRules" label="Email*" required></v-text-field>
            </v-flex>

            <v-flex xs12>
              <v-text-field 
              :append-icon="show ? 'visibility' : 'visibility_off'"
              :type="show ? 'text' : 'password'"
              v-model="password" 
              @click:append="show = !show"
              :rules="inputRules" 
              label="Password*" 
              required></v-text-field>
            </v-flex>
            <small>*indicates required field</small>
          </v-layout>
        </v-container>
      </v-card-text>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="blue darken-1" style="min-width:100px;min-height:50px;" flat @click="dialog=false">Close</v-btn>
        <v-btn color="blue darken-1" style="min-width:100px;min-height:50px;" flat @click="login">Submit</v-btn>
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
import firebase from 'firebase/app'
import 'firebase/auth'

export default {
    data() {
      return {
        user: '',
        email:'',
        password: '',
        dialog: false,
        show: false,
        inputRules: [
            v => v.trim() !== '' || 'You cannot leave this field empty'
        ],
        success: false
      }
    },
    methods: {
        login: function(e) {
        if(this.$refs.form.validate()) {
            firebase.auth().signInWithEmailAndPassword(this.email, this.password).then(cred => {
                alert('You are logged in as ' + this.email);
                this.sucess = true;
                this.$router.push('/dashboard');
                console.log("Login was successful!");
                console.log("");
                console.log(cred.user);

            })
            .catch(error => {
            // Handle Errors here.
                var errorCode = error.code;
                var errorMessage = error.message;
                if (errorCode === 'auth/wrong-password') {
                    alert('You have typed in the wrong password.');
                }

                if (errorCode === 'auth/invalid-email') {
                    alert('Please use a valid email')
                } else if (errorCode === 'auth/user-not-found') {
                    alert('Oops! There is no user found in our database under the email you have provided. Maybe try signing up?')
                } else {
                    alert(errorMessage);
                }
                console.log(error);

            });
            if (this.success === true) {
                this.dialog = false;
            }

        }

        }
      }
}
</script>
