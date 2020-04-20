package twofer

import "strings"

// ShareWith returns a string based on if a user passed a name in.
func ShareWith(name string) string {
	// Create a string builder.
	var sb strings.Builder
	// Write the start of the string
	sb.WriteString("One for ")
	// Write the remainder depending on if there is a name.
	if name == "" {
		sb.WriteString("you, one for me.")
	} else {
		sb.WriteString(name + ", one for me.")
	}
	// Return the finished string builder as a string representation
	return sb.String()
}
