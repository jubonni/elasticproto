const searchResults = await client.elasticsearchClient({
  // Alias pointing to the knowledge base indices.
  index: "knowledge-search", 
  body: {
    size: 3,
    query: {q
      bool: {
        should: [
          // Keyword-search Component. 
          {
            multi_match: {
              query,
              // For queries with 3+ words, at least 49% must match.
              minimum_should_match: "1<-1 3<49%", 
              type: "cross_fields",
              fields: [
                "title",
                "summary",
                "body",
                "id",
              ],
            },
          },
          {
            multi_match: {
              query,
              type: "phrase",
              boost: 9,
              fields: [
                // Stem-based versions of our fields. 
                "title.stem",
                "summary.stem",
                "body.stem",
              ],
            },
          },
          // Semantic Search Component.
          {
            text_expansion: {
              "ml.inference.title_expanded.predicted_value": {
                model_id: ".elser_model_2",
                model_text: query,
              },
            },
          },
          {
            text_expansion: {
              "ml.inference.summary_expanded.predicted_value": {
                model_id: ".elser_model_2",
                model_text: query,
              },
            },
          },
        ],
      },
    },
  },
});
