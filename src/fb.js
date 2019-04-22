import firebase from 'firebase/app'
import 'firebase/firestore'

// Initialize Firebase
var config = {
    apiKey: "AIzaSyBmgfnOfvgC-_6lj56KBsuG5J2s29PdIlo",
    authDomain: "blogdatabase-39a1c.firebaseapp.com",
    databaseURL: "https://blogdatabase-39a1c.firebaseio.com",
    projectId: "blogdatabase-39a1c",
    storageBucket: "blogdatabase-39a1c.appspot.com",
    messagingSenderId: "789831703195"
};
firebase.initializeApp(config);
const db = firebase.firestore();
//db.settings({ timestampsInSnapshots: true });
export default db;
