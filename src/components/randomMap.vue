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
            location: {
                origin: "",
                dest: "",
            },
            result: 'Sydney'
        };
    }, 
    methods: { 
    getURL: function() {
        const path = 'http://localhost:5000/location';
        axios.get(path)
            .then((res) => {
                this.result = res.data.location[0]["end"];
                return this.result
            });
        this.url ="https://maps.google.com/maps?q=" +this.result+"&t=&z=13&ie=UTF8&iwloc=&output=embed" 
    },
},
  created() {
    this.getURL();
  },
};

</script>
