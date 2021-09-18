app.component('urls-table', {
  data() {
    return {
      urls: [],
    }
  },
  props: ['host'],
  watch: {
    currentPage(page) {
      this.updateURLs();
    }
  },
  methods: {
    shortenedAddress(slug) {
      return this.host + 'u/' + slug;
    },
    updateURLs() {
      axios
          .get('/shortener/urls')
          .then(response => {
            this.urls = response.data.results;
          })
          .catch(error => {
            console.log(error);
          });
    },
  },
  mounted() {
    this.updateURLs();
  },
  template: `
    <div class='container text-center'>
        <button v-if='!urls.length' class="btn btn-primary m-3">
            در حال بارگذاری...
            <span class="spinner-border spinner-border-sm"></span>
        </button>
        <table v-else class='table table-bordered table-responsive-sm 
            table-sm table-light table-striped text-center shadow'>
            <thead class='thead-dark'>
                <tr>
                    <th>ردیف</th>
                    <th>برچسب</th>
                    <th>لینک کوتاه</th>
                    <th>بازدیدها</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for='(url, index) in urls'>
                    <td>{{ index }}</td>
                    <td>{{ url.label }}</td>
                    <td><a :href='shortenedAddress(url.slug)'>{{ shortenedAddress(url.slug) }}</a></td>
                    <td>{{ url.visits }}</td>
                </tr>
            </tbody>
        </table>
    </div>
  `
});