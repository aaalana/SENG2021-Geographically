<template>
  <v-footer id="core-footer" absolute height="60">
    <v-layout justify-center row wrap>
      <span v-for="link in links" :key="link.name" color="black">
        <a id="links" :href="link.Link" class="tertiary--text footer-links">{{ link.name }}</a>
      </span>
      

      <v-spacer/>
      
      <span id="copyright" class="font-weight-light copyright"> &copy; {{ (new Date()).getFullYear() }} TeamA | All rights reserved </span>
    </v-layout>
  </v-footer>
</template>

<script>
export default {
  data: () => ({
    links: [
      { name: 'Contact Us', Link: '/contactUs' },
      { name: 'FAQs', Link: '/FAQs' }
    ]
  })
}
</script>

<style>
#core-footer {
  z-index: 0;
}

#links {
  padding: 20px;
  color: rgb(50, 50, 50);
}

#copyright {
  padding-right: 20px;
}
</style>
