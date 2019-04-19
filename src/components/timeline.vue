<template>        
    <v-timeline
        dense
        align-top
    >
        <v-timeline-item
            small
            fill-dot
        >
            <v-layout pt-6>
                <v-flex xs9 sm9 md9>
                <v-form>
                    <v-text-field
                        style="font-family:Quicksand; font-size:15px;"
                        solo
                        label="Search"
                        prepend-inner-icon="place"
                        v-model="location.origin"
                    ></v-text-field>
                </v-form>
                </v-flex>
                <v-flex>
                    <v-btn flat icon small active @click="display = add">
                        <v-icon class="primary--text">add</v-icon>
                    </v-btn>
                </v-flex>
            </v-layout>
        </v-timeline-item>
        <v-timeline-item
            small
            fill-dot
        >
            <v-layout pt-6>
                <v-flex xs9 sm9 md9>
                <v-form>
                    <v-text-field
                        style="font-family:Quicksand; font-size:15px;"
                        solo
                        label="Search"
                        prepend-inner-icon="place"
                        v-model="location.dest"
                        @keyup.native.enter="sendInfo()"
                    ></v-text-field>
                    <v-btn @click="sendInfo()">submit</v-btn>
                </v-form>
                </v-flex>
                <v-flex>
                    <v-btn flat icon small active @click="display = add">
                        <v-icon class="primary--text">add</v-icon>
                    </v-btn>
                </v-flex>
            </v-layout>
        </v-timeline-item>
    </v-timeline>
</template>

<script>
import axios from 'axios';
export default {
    data() {
        return {
            location: {
                origin: "",
                dest: "",
            },
        };
    }, 
    methods: {
    getLocation() {
      const path = 'http://localhost:5000/location';
      axios.get(path)
        .then((res) => {
          this.result = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    sendInfo(origin, dest) {
        const path = 'http://localhost:5000/location';
        axios.post(path,{
            start: this.location.origin,
            end: this.location.dest,
        }
        )
        .then(() => {
            console.log(dest);
            //this.result = this.getLocation()
            console.log(this.result); 
        })
        .catch((err) => {
            console.log(err)
        });
      }
    },
    initForm() {
      this.location.origin = this.location.origin;
      this.location.dest = this.location.dest;
    },
    onSubmit() {
      //evt.preventDefault();
      this.sendInfo();
      this.getLocation();
      this.reloadPage();
    },
    reloadPage(){
        window.location.reload()
    },
  created() {
    this.getLocation();
  },
};

</script>
