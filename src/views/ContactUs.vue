<template>
  <div class="contactUs">
    <h1>This is the contact page</h1>
    <ContactUs />
    <NavBar />
    <Footer />
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
import Footer from '@/components/Footer.vue'

export default {
  components: {
    NavBar,
    Footer
  }
}
</script>
