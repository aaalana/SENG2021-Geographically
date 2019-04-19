<template>
    <div id="singleBlog">
        <v-btn round style="border-radius:7px; width:250px; height:50px;" color="info" class="font-weight-regular subheading" dark>VIEW BLOG POST</v-btn>
        uhgdsvkl
        <h1></h1>
        <article></article>
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
        db.collection('posts').doc(this.id).get().then(snapshot => {
            // snapshot.doc = all docs from database
            // forEach = looping through docs
            snapshot.docs.forEach(doc => {
                //this.posts.push(doc.data())
                const singlePost = doc.data();
                console.log(doc.data())
            })
        })
    }
}
</script>