<template>
    <iframe
        id="gmap_canvas"
        width="100%"
        height="100%"
        :src="this.url"
        frameborder="0"
        scrolling="yes"
        marginheight="0"
        marginwidth="0"
    > </iframe>
</template>

<script>
import axios from 'axios';
export default {
    data() {
        return {
            origin: "",
            dest: "",
            result: 'Sydney',
            url: '' 
        };
    }, 
    methods: { 
    getURL: function() {
        const path = 'http://localhost:5000/trips';
        axios.get(path)
            .then((res) => {
                this.origin = res.data["start"].split(' ').join('+');
                this.dest = res.data["end"].split(' ').join('+');
                this.url = "https://www.google.com/maps/embed/v1/directions?key=AIzaSyAFkE9C-jZGN-bocvETUHsJFm-F0cEhrVE&origin="+this.origin+"&destination="+this.dest
                //this.url ="https://maps.google.com/maps?q=" +this.result+"&t=&z=13&ie=UTF8&iwloc=&output=embed" 
            });
    },
},
  created() {
    this.getURL();
  },
};

</script>
