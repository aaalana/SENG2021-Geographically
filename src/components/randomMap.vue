<template>
    <iframe
        id="gmap_canvas"
        width="100%"
        height="200%"
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
            result: 'hi'
        };
    }, 
    methods: { 
    getURL: function() {
        const path = 'http://localhost:5000/location';
        axios.get(path)
            .then((res) => {
                this.result = res.data.location[0]["end"];
                return this.result
                //alert(this.result) <= this alert would return the location e.g. "Canberra"
            });
        alert(this.result) //<= this alert only returns "hi" from default despite working in line 44
        this.url ="https://maps.google.com/maps?q=" +this.result+"&t=&z=13&ie=UTF8&iwloc=&output=embed" 
        //I want to get this url and put it in the HTML to return a map. The url is passed to HTML if i just put a complete URL
        //but i want to get locations, concatenate into a URL and return maps of that location
        //this.url ="https://maps.google.com/maps?q=" +"Canberra"+"&t=&z=13&ie=UTF8&iwloc=&output=embed" <= this works
    },
},
  created() {
    this.getURL();
  },
};

</script>
