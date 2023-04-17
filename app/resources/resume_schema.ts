interface SummaryLink {
  type: 'linkedin' | 'github' | 'twitter' | 'website'
  url: URL
}

interface Summary {
  name: string
  email: string
  phone?: string
  links?: Array<SummaryLink>
  objective?: string
}

interface ExperienceItem {
  company: string
  title: string
  startDate: Date
  endDate?: Date
  description?: string
  highlights: string[]
}

interface EducationItem {
  institution: string
  program: string
  startDate: Date
  endDate?: Date
  highlights?: string[]
}

interface Project {
  title: string
  url?: URL
  description?: string[]
  highlights?: string[]
}

interface Certification {
  institution: string
  title: string
}

interface Resume {
  summary: Summary
  work: Array<ExperienceItem>
  education: Array<EducationItem>
  projects?: Array<Project>
  certifications?: Array<Certification>
  skills?: Array<string>
}
