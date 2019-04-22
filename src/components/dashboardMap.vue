<template>
    <iframe
        id="gmap_canvas"
        width="100%"
        height="500px"
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
            location: "UNSW",
            url: ""
        };
    }, 
    methods: { 
    getURL: function() {
        const path = 'http://localhost:5000/current';
        axios.get(path)
            .then((res) => {
                this.location = res.data["lat"]+","+res.data["lng"]
                this.url ="https://maps.google.com/maps?q=" +this.location+"&t=&z=13&ie=UTF8&iwloc=&output=embed" 
            });
    },
},
  created() {
    this.getURL();
  },
};

</script>
