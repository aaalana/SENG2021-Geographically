<template>
    <v-dialog
        ref="dialog"
        v-model="modal2"
        :return-value.sync="time"
        persistent
        lazy
        full-width
        width="290px"
    >
        <template v-slot:activator="{ on }">
        <v-text-field
            style="font-family:Quicksand; font-size:15px;"
            v-model="time"
            label="Time"
            append-icon="access_time"
            readonly
            v-on="on"
        ></v-text-field>
        </template>
        <v-time-picker
            v-if="modal2"
            v-model="time"
            full-width
        >
            <v-spacer></v-spacer>
            <v-btn style="font-family:Quicksand; font-size:15px;" flat color="primary" @click="modal2 = false">Cancel</v-btn>
            <v-btn style="font-family:Quicksand; font-size:15px;" flat color="primary" @click="submit">OK</v-btn>
            {{time}}
        </v-time-picker>
    </v-dialog>
</template>

<script>
export default {
    data () {
        return {
            time: null,
            menu2: false,
            modal2: false
        }
    },
    methods: {
        submit: function() {
        this.$refs.dialog.save(this.time)
        this.$emit("inputData", this.time);
        }
    }


};
</script>

