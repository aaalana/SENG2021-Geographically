<template>
    <v-layout>
        <v-menu 
            ref="menu"
            v-model="menu"
            :close-on-content-click="false"
            :nudge-right="40"
            :return-value.sync="date"
            lazy
            transition="scale-transition"
            offset-y
            full-width
            min-width="290px"
        >
        </v-menu>
        <v-dialog 
            ref="dialog"
            v-model="modal"
            :return-value.sync="date"
            persistent
            lazy
            full-width
            width="290px"
        >
            <template v-slot:activator="{ on }">
            <v-text-field
                style="font-family:Quicksand; font-size:15px;"
                v-model="date"
                label="Date"
                append-icon="event"
                readonly
                v-on="on"
            ></v-text-field>
            </template>
            <v-date-picker v-model="date" scrollable>
            <v-spacer></v-spacer>
            <v-btn style="font-family:Quicksand; font-size:15px;" flat color="primary" @click="modal = false">Cancel</v-btn>
            <v-btn style="font-family:Quicksand; font-size:15px;" flat color="primary" @click="$refs.dialog.save(date)">OK</v-btn>
            </v-date-picker>
        </v-dialog>
    </v-layout>
</template>

<script>
export default {
    data: () => ({
      date: new Date().toISOString().substr(0, 10),
      menu: false,
      modal: false,
      menu2: false
    })
}
</script>

