 <template>
  <form id="signup-form">
    <v-btn color="normal" style= "font-family:Quicksand" border-radius=0px flat dark right @click="dialog = true">Sign Up</v-btn>
    <v-layout row justify-center style="width:10px;height:10px;">
    <v-dialog v-model="dialog" dark no-click-animation persistent max-width="600px">

    <v-card>
      <v-form ref="form">
      <v-card-title>
        <span class="headline" colour=white >Sign Up</span>
      </v-card-title>

      <v-card-text>
        <v-container grid-list-md>
          <v-layout wrap>
            <v-flex xs12>
              <v-text-field v-model="user" :rules="inputRules" label="Username*" required></v-text-field>
            </v-flex>

            <v-flex xs12>
              <v-text-field v-model="email" :rules="inputRules" label="Email*" required></v-text-field>
            </v-flex>

            <v-flex xs12>
              <v-text-field v-model="password" :rules="inputRules" label="Password*" type="password" required></v-text-field>
            </v-flex>
            <small>*indicates required field</small>
          </v-layout>
        </v-container>
      </v-card-text>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="blue darken-1" style="min-width:100px;min-height:50px;" flat @click="dialog=false">Close</v-btn>
        <v-btn color="blue darken-1" style="min-width:100px;min-height:50px;" flat @click="signUserUp">Submit</v-btn>
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
        success: false
      }
    },
    methods: {
      signUserUp: function(e) {
        // still need to check that user name is not taken
        if(this.$refs.form.validate()) {
          firebase.auth().createUserWithEmailAndPassword(this.email, this.password).then(user => {
            const newUser = {
              id: user.uid,
              username: this.user,
              address: '',
              registeredBlogPosts: []
            }
            /*
            return user.updateProfile ({
              displayName: document.getElementById(this.user).value
            })*/

            this.success = true;
            alert('Account created for ' + this.email);
            this.$router.push('/dashboard');
            console.log("Sign up was successful!");

          })
          .catch(error => {
           // Handle Errors here.
            var errorCode = error.code;
            var errorMessage = error.message;
            if (errorCode === 'auth/weak-password') {
              alert('The password is too weak. Please make a password that is at least 6 characters long.');
            } else if (errorCode === 'auth/email-already-in-use') {
              alert('The email is already in use')
            } else if(errorCode === 'auth/invalid-email') {
              alert('Please use a valid email')
            } else {
              alert(errorMessage);
            }
            console.log(error);
          });
          /*
          firebase.auth().currentUser.sendEmailVerification(actionCodeSettings)
          .then(function() {
            // Verification email sent.
          })
          .catch(function(error) {
            // Error occurred. Inspect error.code.
          });
          */
          if (this.success === true) {
            this.dialog = false;
          }
      }
    }
  }
}
</script>
