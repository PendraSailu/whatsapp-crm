<template>
  <div class="p-4 bg-white shadow rounded">
    <h2 class="text-xl font-bold mb-2">Generate a Message</h2>
    <input v-model="prompt" placeholder="Enter your prompt (e.g., Diwali wish)" class="border p-2 w-full mb-2"/>
    <button @click="generateMessage" class="bg-blue-500 text-white px-4 py-2 rounded">Generate</button>
    
    <div v-if="generatedMessage" class="mt-4">
      <h3 class="font-semibold">Generated Message:</h3>
      <textarea v-model="generatedMessage" class="border p-2 w-full h-24"></textarea>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      prompt: "",
      generatedMessage: ""
    };
  },
  methods: {
    async generateMessage() {
      try {
        const res = await axios.post("http://localhost:8000/messages/generate-message/", {
          prompt: this.prompt,
          name: "{name}"
        });
        this.generatedMessage = res.data.generated_message;
      } catch (err) {
        console.error(err);
      }
    }
  }
};
</script>
