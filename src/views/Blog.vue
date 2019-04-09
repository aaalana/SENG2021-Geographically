<template>
    <div class="blog">
        <v-content>
            <link href='https://fonts.googleapis.com/css?family=Quicksand' rel='stylesheet'>
            <v-flex mb-4>
                <h1 class="display-2 font-weight-bold mb-3">
                    <br>My Blog
                </h1>
                <h1 class="display-1 font-weight-bold mb-3">
                    <br>Posts
                </h1>
                <AddPost />
            </v-flex>
            <v-container class="my-5">
                    <v-card v-for="blog in blogs" :key="blog.title">
                        <v-layout row wrap :class="'pa-3 blog ${blog.status}'"> 
                            <v-flex>
                                <v-icon large left>description</v-icon>
                                <span class="headline">{{ blog.title }}</span>
                            </v-flex>
                            <v-flex>
                            <v-card-actions>
                                <EditPost />
                                <v-btn flat fab><v-icon>delete</v-icon></v-btn>
                            </v-card-actions>
                            </v-flex>

                            <v-flex> <div class="caption grey--text">Date</div><div>{{ blog.date}}</div></v-flex>
                            <!--<v-flex> <div class="caption grey--text">Status</div><div>{{blog.status}}</div></v-flex>-->
                            
                            <v-spacer></v-spacer>

                            <v-flex>
                            <v-card-actions class="text-xs-center">
                                <v-btn round style="border-radius:7px; width:250px; height:50px;" color="info" class="font-weight-regular subheading" dark>VIEW BLOG POST</v-btn>
                            </v-card-actions>
                            </v-flex>
                        </v-layout>
                    </v-card>
                </v-container>
        </v-content>
        <Menu />
    </div>
</template>

<script>
// @ is an alias to /src
import Menu from '@/components/Menu.vue'
import AddPost from '@/components/AddPost.vue'
import EditPost from '@/components/EditPost.vue'
export default {
  name: 'blog',
  components: {
    Menu,
    AddPost,
    EditPost
  },
  data() {
      return {
          blogs: [
              {title: 'blog1', date: '1/2/19'},
              {title: 'blog2', date: '2/3/19'}
          ]
      }
  }
}
</script>

<style>
.blog.published {
    border-left: 4px solid #3cd1c2;

}

.blog.draft {
    border-left: 4px solid orange;
}
</style>