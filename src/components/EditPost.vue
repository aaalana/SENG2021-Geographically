<template>
    <v-dialog max width="1450px" v-model="dialog">
        <v-btn flat fab slot="activator"><v-icon>edit</v-icon></v-btn>
            <v-layout row wrap>
            <v-card min width="725px" class="px-5">
                <v-card-title>
                    <h2>Edit Blog Post</h2>
                </v-card-title>
                <v-card-text>
                    <v-form ref="">
                        <v-text-field label="Title" v-model="title" prepend-icon="folder" :rules="inputRules"></v-text-field>
                        <v-textarea label="Information" v-model="content" prepend-icon="edit" :rules="inputRules"></v-textarea>

                        <v-menu>
                            <v-text-field :rules="inputRules" :value="date" slot="activator" label="Date" prepend-icon="date_range"></v-text-field>
                            <v-date-picker v-model="date"></v-date-picker>
                        </v-menu>
                        
                        <v-spacer></v-spacer>

                        <v-btn flat class="info mx-0 mt-3" @click="publish" :loading="loading">Save and Publish</v-btn>
                    </v-form>
                </v-card-text>
            </v-card>
             <v-card min width="725px" class="px-5">
                <v-card-title>
                    <h2>Preview</h2>
                </v-card-title>
                <v-card-text>
                    <h2>{{ title }}</h2>
                    <v-layout row justify-start align-start>
                        <v-flex class="caption grey--text">Written by user</v-flex>
                        <v-flex class="caption grey--text">Published on {{ date }}</v-flex>
                    </v-layout>
                    <br>
                    <p>{{ content }}</p>
                </v-card-text>
            </v-card>
            </v-layout>
    </v-dialog>
</template>

<script>
export default {
    data() {
        return {
            title: '',
            content: '',
            date: null,
            inputRules: [
                v => v.length > 3 || 'Minimum length is 3 characters'
            ],
            loading: false,
            dialog: false
        }
    },
    methods: {
        publish() {
            if(this.$refs.form.validate()) {
                //this.loading = true; //use this when we actually put it in the database to show a loading sign
                this.dialog = false;
                //console.log(this.title, this.content)
                this.loading = false;
               
            }
        }
    }
}
</script>