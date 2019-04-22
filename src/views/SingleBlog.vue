<template>
    <div id="singleBlog">
    <v-container>
        <link href='https://fonts.googleapis.com/css?family=Quicksand' rel='stylesheet'>
        <h1 style="font-family: Quicksand;">{{ post.title }}</h1>
        <v-layout row justify-start align-start>
            <v-flex pr-4 xs4 md4 class="grey--text" style="word-wrap: break-word;">Written by {{ post.user }}</v-flex>
            <v-flex xs4 md4 class="grey--text" style="word-wrap: break-word;">Modified on {{ post.date }}</v-flex>
            <v-flex v-if="post.locationRated !== ''">
            <div xs4 md4 class="caption grey--text" style="word-wrap: break-word;"><v-icon small class="mr-1">location_on</v-icon>{{ post.locationRated }}</div>
                <v-rating
                class="ml-3"
                v-model="post.rating"
                background-color="yellow accent-4"
                color="yellow accent-4"
                dense
                small
                half-increments
                readonly
                size="20"
                ></v-rating>
            </v-flex>
        </v-layout>
         <br>
        <div v-html="post.content"></div>
    </v-container>
    </div>
</template>

<script>
import db from '@/fb'
export default {
    data() {
        return {
            // take route parameter from url named id and store it into id data
            id: this.$route.params.id,
            post: {}
        }
    },
    created() {
        db.collection('posts').doc(this.id).get().then(doc => {
            this.post = doc.data();
            console.log(doc.data())
        });
    }
}
</script>