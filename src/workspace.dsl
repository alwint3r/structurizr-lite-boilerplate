workspace "SoftwareArchitecture" "This is a model for a software architecture" {
    model {
        user = person "User"
        software = softwareSystem "Software System"

        user -> software "Uses"
    }

    views {
        themes "https://structurizr.com/share/36141/theme"
        systemContext software "SystemContext" "An example of system context diagram" {
            include *
            autoLayout
        }
    }
}