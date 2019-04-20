<template>
    <div id="singleBlog">
    <v-container>
        <link href='https://fonts.googleapis.com/css?family=Quicksand' rel='stylesheet'>
        <h1 style="font-family: Quicksand;">{{ post.title }}</h1>
        <v-layout row justify-start align-start>
            <v-flex pr-4 xs6 md6 class="grey--text" style="word-wrap: break-word;">Written by {{ post.user }}</v-flex>
            <v-flex xs6 md6 class="grey--text" style="word-wrap: break-word;">Modified on {{ post.date }}</v-flex>
        </v-layout>
         <br>
        <article>{{ post.content }}</article>
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
            // snapshot.doc = all docs from database
            // forEach = looping through docs
            this.post = doc.data();
            console.log(doc.data())
        })
    }
}
</script>