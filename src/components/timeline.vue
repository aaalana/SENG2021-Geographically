<template>        
    <v-timeline
        dense
        align-top
    >
        <v-timeline-item
            small
            v-for="(item, i) in items"
            :key="i"
            :color="item.colour"
            :icon="item.icon"
            fill-dot
        >
            <v-layout pt-6>
                <v-flex xs9 sm9 md9>
                <v-form>
                    <v-text-field
                        style="font-family:Quicksand; font-size:15px;"
                        solo
                        label="Search"
                        prepend-inner-icon="place"
                    ></v-text-field>
                </v-form>
                </v-flex>
                <v-flex>
                    <v-btn flat icon small active @click="display = add">
                    <v-icon class="primary--text">add</v-icon>
                </v-btn>
                </v-flex>
            </v-layout>
        </v-timeline-item>
    </v-timeline>
</template>

<script>
export default {
    data: () => ({
      items: [
        {
            colour: 'blue darken-2',
            icon: 'looks_one'
        },
        {
            colour: 'blue darken-2',
            icon: 'looks_two'
        }
      ]
    })
}
</script>
