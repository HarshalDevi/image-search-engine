package main

import (
	"bufio"
	"context"
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"os/exec"
	"strings"

	pb "image_search_engine" // Import the generated protobuf package

	"google.golang.org/grpc"
)

func run(keyword string, client pb.ImageSearchClient) {
	// Create a context and make the RPC call to the server
	ctx := context.Background()
	response, err := client.SearchImage(ctx, &pb.SearchRequest{Keyword: keyword})
	if err != nil {
		log.Fatalf("Error calling SearchImage: %v", err)
	}

	// Process the response
	if len(response.GetImageData()) > 0 {
		// Save the image data to a file
		filename := keyword + ".jpg"
		if err := ioutil.WriteFile(filename, response.GetImageData(), 0644); err != nil {
			log.Fatalf("Error writing image data to file: %v", err)
		}
		log.Printf("Image received successfully for keyword '%s'", keyword)

		// Open the image file
		if err := openFile(filename); err != nil {
			log.Printf("Error opening image file: %v", err)
		}
	} else {
		log.Printf("No image found for the keyword '%s'", keyword)
	}
}

func openFile(filename string) error {
	cmd := exec.Command("explorer", filename)

	if err := cmd.Run(); err != nil {
		return err
	}
	return nil
}

func main() {
	// Set up a connection to the server.
	conn, err := grpc.Dial("localhost:50051", grpc.WithInsecure())
	if err != nil {
		log.Fatalf("Failed to dial server: %v", err)
	}
	defer conn.Close()

	// Create a client stub
	client := pb.NewImageSearchClient(conn)

	// Prompt the user to enter the keyword
	fmt.Print("Enter keyword: ")
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	keyword := strings.TrimSpace(scanner.Text())

	if keyword == "" {
		log.Fatal("Keyword cannot be empty")
	}

	run(keyword, client)
}
